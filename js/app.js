import { createClient } from 'https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2/+esm';

console.log("App.js loaded");
// 1. Initialize Supabase
const SUPABASE_URL = 'https://brudufqolikgmecykdnj.supabase.co';
const SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJydWR1ZnFvbGlrZ21lY3lrZG5qIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODQ3NjAxMzcsImV4cCI6MjEwMDMzNjEzN30.8ZvnWRRcScCnm5CuVDnkHc0u_i_CW_w5U4hQWm5hPXw';
const supabase = createClient(SUPABASE_URL, SUPABASE_ANON_KEY);

// 2. Dynamic Form Submission Handler
document.addEventListener('DOMContentLoaded', () => {
  const forms = document.querySelectorAll('[data-supabase-form]');

  forms.forEach(form => {
  form.addEventListener("submit", async (e) => {
  e.preventDefault();

  console.log("Submit clicked");

  const tableName = form.getAttribute("data-supabase-form");
  console.log("Table:", tableName);

  const formData = new FormData(form);
  const payload = Object.fromEntries(formData.entries());

  console.log(payload);

  console.log("Cabin Class =", formData.cabin_class);
  const { data, error } = await supabase
    .from(tableName)
    .insert([payload])
    .select();

  console.log("Data:", data);
  console.dir(error);
console.log(JSON.stringify(error, null, 2));
});
  });
});