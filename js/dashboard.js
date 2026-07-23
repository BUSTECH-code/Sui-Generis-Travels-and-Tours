import { supabase } from "./supabase.js";

const { data } = await supabase.auth.getSession();

if (!data.session) {

    window.location.href = "../admin/login.html";

}

const SUPABASE_URL = "https://brudufqolikgmecykdnj.supabase.co";
const SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJydWR1ZnFvbGlrZ21lY3lrZG5qIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODQ3NjAxMzcsImV4cCI6MjEwMDMzNjEzN30.8ZvnWRRcScCnm5CuVDnkHc0u_i_CW_w5U4hQWm5hPXw";

const TABLES = {

    bookings: {
        title: "Flight Bookings",
        countId: "stat-bookings",
        columns: [
            "fullname",
            "phone",
            "departure_city",
            "destination_city",
            "departure_date",
            "status"
        ]
    },

    visa_applications: {
        title: "Visa Applications",
        countId: "stat-visas",
        columns: [
            "fullname",
            "destination_country",
            "visa_category",
            "travel_date",
            "status"
        ]
    },

    study_applications: {
        title: "Study Abroad",
        countId: "stat-study",
        columns: [
            "fullname",
            "country",
            "course",
            "qualification",
            "status"
        ]
    },

    appointments: {
        title: "Appointments",
        countId: "stat-appointments",
        columns: [
            "fullname",
            "service",
            "appointment_date",
            "status"
        ]
    },

    contacts: {
    title: "Customer Inquiries",
    countId: "stat-contacts",
    columns: [
        "fullname",
        "email",
        "phone",
        "subject",
        "message",
        "created_at"
    ]
},

    blogs: {
        title: "Blog Manager",
        countId: "stat-blogs",
        columns: [
            "title",
            "published",
            "created_at"
        ]
    },

    gallery: {
        title: "Gallery Manager",
        countId: "stat-gallery",
        columns: [
            "title",
            "category",
            "created_at"
        ]
    },

    testimonials: {
        title: "Testimonials",
        countId: "stat-testimonials",
        columns: [
            "name",
            "rating",
            "approved"
        ]
    },

    newsletter: {
        title: "Newsletter Subscribers",
        countId: "stat-newsletter",
        columns: [
            "email",
            "created_at"
        ]
    },

    special_offers: {
        title: "Special Offers",
        countId: "stat-offers",
        columns: [
            "title",
            "expires_at",
            "active"
        ]
    }

};

const STATUS_OPTIONS = ["pending","processing","confirmed","completed","cancelled"];

let currentTable = "home";
const state = {
    records: [],
    filteredRecords: [],
    currentPage: 1,
    pageSize: 8,
    searchTerm: "",
    statusFilter: "",
    sortField: "",
    sortAscending: true,
    loading: false,
    totalCount: 0,
    pages: 1
};

const searchInput = document.getElementById("search-input");
const sortFieldSelect = document.getElementById("sort-field");
const sortToggleBtn = document.getElementById("sort-toggle");
const statusFilterInput = document.getElementById("status-filter");
const previousPageBtn = document.getElementById("previous-page");
const nextPageBtn = document.getElementById("next-page");
const pageIndicator = document.getElementById("page-indicator");
const toastContainer = document.getElementById("toast-container");
const modalBackdrop = document.getElementById("record-modal");
const modalBody = document.getElementById("modal-body");
const modalClose = document.getElementById("modal-close");
const homeSection = document.getElementById("home-section");
const tableSection = document.getElementById("table-section");
const pageTitle = document.getElementById("page-title");
const pageDescription = document.getElementById("page-description");
const TOAST_DURATION = 4200;

document.addEventListener("DOMContentLoaded", () => {

    initialiseNavigation();
    initialiseToolbar();
    loadDashboardStats();
    showDashboardHome();

});

function updateActiveNav(moduleName) {
    document.querySelectorAll(".nav-item[data-table]").forEach(nav => {
        nav.classList.toggle("active", nav.dataset.table === moduleName);
    });
}

function initialiseNavigation(){

    document.querySelectorAll(".nav-item[data-table]").forEach(item=>{

        item.addEventListener("click",()=>{

            updateActiveNav(item.dataset.table);
            currentTable = item.dataset.table || "home";
            state.currentPage = 1;
            state.searchTerm = "";
            state.statusFilter = "";
            if (searchInput) searchInput.value = "";
            if (statusFilterInput) statusFilterInput.value = "";

            if (currentTable === "home") {
                showDashboardHome();
                return;
            }

            if (!TABLES[currentTable]) {
                showToast("Table configuration is missing.", "error");
                showDashboardHome();
                return;
            }

            loadTable(currentTable);

        });

    });

}

function initialiseToolbar(){
    if (searchInput) {
        searchInput.addEventListener("input", event => {
            state.searchTerm = event.target.value.trim();
            state.currentPage = 1;
            applyFiltersAndRender();
        });
    }

    if (sortFieldSelect) {
        sortFieldSelect.addEventListener("change", event => {
            state.sortField = event.target.value;
            state.currentPage = 1;
            applyFiltersAndRender();
        });
    }

    if (sortToggleBtn) {
        sortToggleBtn.addEventListener("click", () => {
            state.sortAscending = !state.sortAscending;
            applyFiltersAndRender();
        });
    }

    if (statusFilterInput) {
        statusFilterInput.addEventListener("change", event => {
            state.statusFilter = event.target.value;
            state.currentPage = 1;
            applyFiltersAndRender();
        });
    }

    if (previousPageBtn) {
        previousPageBtn.addEventListener("click", () => {
            if (state.currentPage > 1) {
                state.currentPage -= 1;
                applyFiltersAndRender();
            }
        });
    }

    if (nextPageBtn) {
        nextPageBtn.addEventListener("click", () => {
            if (state.currentPage < state.pages) {
                state.currentPage += 1;
                applyFiltersAndRender();
            }
        });
    }

    if (modalClose) {
        modalClose.addEventListener("click", closeModal);
    }

    if (modalBackdrop) {
        modalBackdrop.addEventListener("click", event => {
            if (event.target === modalBackdrop) {
                closeModal();
            }
        });
    }

    document.addEventListener("change", async event => {
        const select = event.target.closest(".record-status");
        if (!select) return;

        const id = select.dataset.id;
        const newStatus = select.value;
        const record = getRecordById(id);
        if (!record) {
            showToast("Record not found.", "error");
            return;
        }

        const { error } = await supabase
            .from(currentTable)
            .update({ status: newStatus })
            .eq("id", id);

        if (error) {
            showToast(error.message || "Status update failed.", "error");
            select.value = record.status || "pending";
            return;
        }

        record.status = newStatus;
        const filteredRecord = state.filteredRecords.find(item => String(item.id) === String(id));
        if (filteredRecord) filteredRecord.status = newStatus;
        showToast("Status updated successfully.", "success");
    });
}

async function loadDashboardStats(){

    for(const tableName in TABLES){

        const {count}=await supabase
        .from(tableName)
        .select("*",{count:"exact",head:true});

        document.getElementById(TABLES[tableName].countId).textContent=count??0;

    }

}

function showDashboardHome() {
    if (pageTitle) pageTitle.textContent = "Dashboard Home";
    if (pageDescription) pageDescription.textContent = "Overview of your travel operations, live status, and quick actions.";
    if (homeSection) homeSection.classList.remove("hidden");
    if (tableSection) tableSection.classList.add("hidden");
}

function showRecordsTable(config) {
    if (!config) return;
    if (pageTitle) pageTitle.textContent = config.title;
    if (pageDescription) pageDescription.textContent = config.description || `Manage ${config.title.toLowerCase()}.`;
    if (homeSection) homeSection.classList.add("hidden");
    if (tableSection) tableSection.classList.remove("hidden");
    if (sortFieldSelect) {
        sortFieldSelect.innerHTML = `<option value="">Sort by</option>${config.columns.map(col => `<option value="${col}">${formatHeading(col)}</option>`).join("")}`;
    }
    if (sortToggleBtn) {
        sortToggleBtn.disabled = !config.columns.length;
    }
}

function resetTableState() {
    state.currentPage = 1;
    state.searchTerm = "";
    state.statusFilter = "";
    state.sortField = "";
    state.sortAscending = true;
    if (searchInput) searchInput.value = "";
    if (statusFilterInput) statusFilterInput.value = "";
    if (sortFieldSelect) sortFieldSelect.value = "";
}

async function loadTable(tableName){
    const config = TABLES[tableName];
    if (!config) {
        showToast("Table configuration is missing.", "error");
        showDashboardHome();
        return;
    }

    currentTable = tableName;
    updateActiveNav(tableName);
    showRecordsTable(config);
    state.currentPage = 1;
    state.searchTerm = "";
    state.statusFilter = "";
    if (searchInput) searchInput.value = "";
    if (statusFilterInput) statusFilterInput.value = "";

    setLoading(true);

    const {data, error} = await supabase
        .from(tableName)
        .select("*")
        .order("created_at", {ascending:false});

    setLoading(false);

    if (error) {
        console.error(error);
        showToast(`Failed to load ${config.title}`, "error");
        state.records = [];
        applyFiltersAndRender();
        return;
    }

    state.records = data ?? [];
    state.currentPage = 1;
    state.totalCount = state.records.length;
    state.pages = Math.max(1, Math.ceil(state.totalCount / state.pageSize));
    applyFiltersAndRender();
}

function applyFiltersAndRender(){
    const config = TABLES[currentTable];
    if (!config) {
        showDashboardHome();
        return;
    }

    let records = [...state.records];

    if (state.statusFilter) {
        records = records.filter(record => {
            const value = String(record.status ?? "").toLowerCase();
            return value === state.statusFilter.toLowerCase();
        });
    }

    if (state.sortField) {
        records.sort((a, b) => {
            const aValue = String(a[state.sortField] ?? "").toLowerCase();
            const bValue = String(b[state.sortField] ?? "").toLowerCase();
            if (aValue === bValue) return 0;
            return state.sortAscending ? aValue.localeCompare(bValue, undefined, {numeric:true, sensitivity:"base"}) : bValue.localeCompare(aValue, undefined, {numeric:true, sensitivity:"base"});
        });
    }

    if (state.searchTerm) {
        const query = state.searchTerm.toLowerCase();
        records = records.filter(record => {
            return Object.values(record).some(value => {
                if (value === null || value === undefined) return false;
                return String(value).toLowerCase().includes(query);
            });
        });
    }

    state.filteredRecords = records;
    state.totalCount = records.length;
    state.pages = Math.max(1, Math.ceil(state.totalCount / state.pageSize));
    if (state.currentPage > state.pages) state.currentPage = state.pages;

    const start = (state.currentPage - 1) * state.pageSize;
    const pageData = records.slice(start, start + state.pageSize);

    renderTable(config, pageData);
    updatePagination();
}

function renderTable(config, data) {
    if (!config) return;
    const head = document.getElementById("table-head");
    const body = document.getElementById("table-body");
    if (!head || !body) return;
    head.innerHTML = "";
    body.innerHTML = "";

    config.columns.forEach(col => {
        head.innerHTML += `
            <th>${formatHeading(col)}</th>
        `;
    });
    head.innerHTML += `<th>Actions</th>`;

    if (state.loading) {
        const span = config.columns.length + 1;
        body.innerHTML = `
            <tr class="loading-row">
                <td colspan="${span}">
                    <div class="loader">Loading records...</div>
                </td>
            </tr>
        `;
        return;
    }

    if (!data.length) {
        const span = config.columns.length + 1;
        body.innerHTML = `
            <tr class="empty-state">
                <td colspan="${span}">
                    No records found. Adjust filters or select a different dataset.
                </td>
            </tr>
        `;
        return;
    }

    data.forEach(record => {
        let row = `<tr>`;
        config.columns.forEach(col => {
            if (col === "status") {
                const currentStatus = (record.status || "pending").toLowerCase();
                const options = STATUS_OPTIONS.map(status => `
                        <option value="${status}" ${status === currentStatus ? "selected" : ""}>
                            ${formatHeading(status)}
                        </option>
                    `).join("");

                row += `
                    <td>
                        <select class="record-status form-control" data-id="${record.id}" aria-label="Select status for ${record.fullname || "record"}">
                            ${options}
                        </select>
                    </td>
                `;
            } else {
                row += `
                    <td>${record[col] ?? "-"}</td>
                `;
            }
        });

        row += `
            <td class="actions">
                <button class="btn-view" data-id="${record.id}" title="View">
                    <i class="fa-solid fa-eye"></i>
                </button>
                <button class="btn-edit" data-id="${record.id}" title="Edit">
                    <i class="fa-solid fa-pen"></i>
                </button>
                <button class="btn-delete" data-id="${record.id}" title="Delete">
                    <i class="fa-solid fa-trash"></i>
                </button>
            </td>
        `;
        row += `</tr>`;
        body.innerHTML += row;
    });
}

function updatePagination(){
    if (!pageIndicator) return;
    pageIndicator.textContent = `Page ${state.currentPage} of ${state.pages} · ${state.totalCount} record${state.totalCount === 1 ? "" : "s"}`;
    if (previousPageBtn) previousPageBtn.disabled = state.currentPage <= 1;
    if (nextPageBtn) nextPageBtn.disabled = state.currentPage >= state.pages;
}

function setLoading(value){
    state.loading = value;
    const config = TABLES[currentTable];
    if (config) {
        renderTable(config, []);
    }
}

function getRecordById(id){
    return state.records.find(item => String(item.id) === String(id));
}

function openModal(record){
    if (!modalBackdrop || !modalBody) return;
    const entries = Object.entries(record || {}).filter(([key]) => key !== "id");
    const bodyContent = entries.map(([key, value]) => {
        const displayValue = value === null || value === undefined ? "-" : String(value);
        return `
            <dt>${formatHeading(key)}</dt>
            <dd>${displayValue}</dd>
        `;
    }).join("");

    modalBody.innerHTML = `
        <dl>${bodyContent}</dl>
    `;
    modalBackdrop.classList.remove("hidden");
}

function closeModal(){
    if (!modalBackdrop) return;
    modalBackdrop.classList.add("hidden");
}

function showToast(message, type = "info"){
    if (!toastContainer) return;
    const toast = document.createElement("div");
    toast.className = `toast ${type}`;
    toast.textContent = message;
    toastContainer.appendChild(toast);
    setTimeout(() => {
        toast.remove();
    }, TOAST_DURATION);
}

function formatHeading(text) {
    return text
        .replaceAll("_", " ")
        .replace(/\b\w/g, l => l.toUpperCase());
}

/* =====================================================
   TABLE ACTIONS
===================================================== */

document.addEventListener("click", async (e) => {

    const button = e.target.closest("button");

    if (!button) return;

    const id = button.dataset.id;

    // VIEW
    if (button.classList.contains("btn-view")) {
        const record = getRecordById(id);
        if (!record) {
            showToast("Record not found.", "error");
            return;
        }
        openModal(record);
        return;
    }

    if (button.classList.contains("btn-edit")) {
        const record = getRecordById(id);
        if (!record) {
            showToast("Record not found.", "error");
            return;
        }
        openModal(record);
        return;
    }

    if (button.classList.contains("btn-delete")) {
        const confirmDelete = confirm("Delete this record permanently?");
        if (!confirmDelete) return;

        const { error } = await supabase
            .from(currentTable)
            .delete()
            .eq("id", id);

        if (error) {
            showToast(error.message || "Delete failed.", "error");
            return;
        }

        showToast("Record deleted successfully.", "success");
        loadTable(currentTable);
    }

});

/* =====================================================
   LOGOUT
===================================================== */

document
    .getElementById("logout-btn")
    .addEventListener("click", async () => {

        await supabase.auth.signOut();

        window.location.href = "login.html";

    });