console.log("App.js loaded");

const GOOGLE_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbxhH0GrzhR_z2ZCak8iCuTTqCm6T9abQZNStfz5fdLbe37mRDV1d6DcWYMs23eLhYyM/exec";
const SHEET_MAP = {
  bookings: "Bookings",
  visa_applications: "Visa Applications",
  study_applications: "Study Applications",
  appointments: "Appointments",
  contacts: "Contacts"
};
const FEEDBACK_DURATION_MS = 4200;

function ensureFeedbackContainer() {
  let container = document.getElementById("public-form-feedback");

  if (!container) {
    container = document.createElement("div");
    container.id = "public-form-feedback";
    container.setAttribute("aria-live", "polite");
    container.setAttribute("aria-atomic", "true");
    document.body.appendChild(container);
  }

  return container;
}

function dismissFeedback(toast) {
  if (!toast || !toast.isConnected) return;

  toast.classList.remove("show");
  toast.classList.add("hide");

  window.setTimeout(() => {
    toast.remove();
  }, 220);
}

function showFeedback(type, title, message) {
  const container = ensureFeedbackContainer();
  const toast = document.createElement("div");
  toast.className = `public-form-feedback ${type}`;
  toast.innerHTML = `
    <div class="feedback-icon" aria-hidden="true">
      ${type === "success" ? "✓" : "!"}
    </div>
    <div class="feedback-content">
      <strong>${title}</strong>
      <p>${message}</p>
    </div>
    <button class="feedback-close" type="button" aria-label="Dismiss notification">×</button>
  `;

  const closeButton = toast.querySelector(".feedback-close");
  closeButton.addEventListener("click", () => dismissFeedback(toast));

  container.appendChild(toast);

  requestAnimationFrame(() => {
    toast.classList.add("show");
  });

  window.setTimeout(() => dismissFeedback(toast), FEEDBACK_DURATION_MS);
}

function setSubmitButtonState(button, isSubmitting) {
  if (!button) return;

  const originalText = button.dataset.originalText || button.textContent.trim();
  button.dataset.originalText = originalText;
  button.disabled = isSubmitting;
  button.classList.toggle("is-submitting", isSubmitting);

  if (isSubmitting) {
    button.innerHTML = `
      <span class="submit-spinner" aria-hidden="true"></span>
      <span>Submitting...</span>
    `;
  } else {
    button.textContent = originalText;
  }
}

function buildPayload(form) {
  const formData = new FormData(form);
  const payload = Object.fromEntries(formData.entries());
  const tableName = form.dataset.supabaseForm;

  payload.formType = SHEET_MAP[tableName] || tableName;
  return payload;
}

async function submitPublicForm(form) {
  const submitButton = form.querySelector("button[type='submit']");

  if (!submitButton) {
    return;
  }

  if (form.dataset.isSubmitting === "true") {
    return;
  }

  form.dataset.isSubmitting = "true";
  setSubmitButtonState(submitButton, true);

  try {
    const payload = buildPayload(form);
    const response = await fetch(GOOGLE_SCRIPT_URL, {
      method: "POST",
      body: new URLSearchParams(payload)
    });

    const responseText = await response.text();
    let parsedResult = null;

    try {
      parsedResult = responseText ? JSON.parse(responseText) : {};
    } catch (error) {
      parsedResult = { raw: responseText };
    }

    const isSuccess = response.ok && parsedResult?.success !== false && parsedResult?.status !== "error" && !/error/i.test(responseText) && !/failed/i.test(responseText);

    if (isSuccess) {
      showFeedback(
        "success",
        "Request received",
        "Your request has been submitted successfully. Our team will contact you shortly."
      );
      form.reset();
    } else {
      const errorMessage = parsedResult?.error || "We couldn't submit your request. Please try again.";
      showFeedback("error", "Submission issue", errorMessage);
    }
  } catch (error) {
    console.error("Google Form submission failed:", error);
    showFeedback("error", "Submission issue", "We couldn't submit your request. Please try again.");
  } finally {
    form.dataset.isSubmitting = "false";
    setSubmitButtonState(submitButton, false);
  }
}

document.addEventListener("DOMContentLoaded", () => {
  const forms = document.querySelectorAll("form[data-supabase-form]");

  forms.forEach((form) => {
    form.addEventListener("submit", async (event) => {
      event.preventDefault();
      await submitPublicForm(form);
    });
  });
});
