from pathlib import Path

html = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Admin Operations Center | SUI-GENERIS</title>
  <link rel="stylesheet" href="../css/dashboard.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.2/css/all.min.css">
</head>
<body>
  <div class="admin-layout">
    <aside class="sidebar">
      <div class="sidebar-brand">
        <img src="../assets/logos/sui generis logo 1.jpg" alt="SUI-GENERIS logo">
        <div>
          <span>SUIGENERIS</span>
          <p>Admin Operations</p>
        </div>
      </div>
      <nav class="sidebar-nav" aria-label="Admin navigation">
        <button type="button" class="nav-item active" data-table="home"><i class="fa-solid fa-house"></i>Dashboard Home</button>
        <button type="button" class="nav-item" data-table="bookings"><i class="fa-solid fa-plane"></i>Flight Bookings</button>
        <button type="button" class="nav-item" data-table="visa_applications"><i class="fa-solid fa-passport"></i>Visa Requests</button>
        <button type="button" class="nav-item" data-table="study_applications"><i class="fa-solid fa-graduation-cap"></i>Study Abroad</button>
        <button type="button" class="nav-item" data-table="appointments"><i class="fa-solid fa-calendar-days"></i>Appointments</button>
        <button type="button" class="nav-item" data-table="contacts"><i class="fa-solid fa-envelope"></i>Inquiries</button>
        <button type="button" class="nav-item" data-table="blogs"><i class="fa-solid fa-newspaper"></i>Blog Manager</button>
        <button type="button" class="nav-item" data-table="gallery"><i class="fa-solid fa-image"></i>Gallery Manager</button>
        <button type="button" class="nav-item" data-table="testimonials"><i class="fa-solid fa-comment-dots"></i>Testimonials</button>
        <button type="button" class="nav-item" data-table="special_offers"><i class="fa-solid fa-tag"></i>Special Offers</button>
        <button type="button" class="nav-item" data-table="newsletter"><i class="fa-solid fa-envelope-open-text"></i>Newsletter</button>
      </nav>
      <button id="logout-btn" class="nav-item nav-signout" type="button"><i class="fa-solid fa-right-from-bracket"></i>Sign Out</button>
    </aside>

    <main class="main-content">
      <div class="top-header">
        <div>
          <h1 id="page-title">Dashboard Home</h1>
          <p id="page-description">Overview of your travel operations, live status, and quick actions.</p>
        </div>
      </div>

      <div class="grid-4 stats-grid" aria-label="Dashboard statistics">
        <section class="card stat-card">
          <p>Flight Bookings</p>
          <h2 id="stat-bookings">0</h2>
        </section>
        <section class="card stat-card">
          <p>Visa Requests</p>
          <h2 id="stat-visas">0</h2>
        </section>
        <section class="card stat-card">
          <p>Study Abroad</p>
          <h2 id="stat-study">0</h2>
        </section>
        <section class="card stat-card">
          <p>Appointments</p>
          <h2 id="stat-appointments">0</h2>
        </section>
        <section class="card stat-card">
          <p>Inquiries</p>
          <h2 id="stat-contacts">0</h2>
        </section>
        <section class="card stat-card">
          <p>Blog Posts</p>
          <h2 id="stat-blogs">0</h2>
        </section>
        <section class="card stat-card">
          <p>Gallery Items</p>
          <h2 id="stat-gallery">0</h2>
        </section>
        <section class="card stat-card">
          <p>Testimonials</p>
          <h2 id="stat-testimonials">0</h2>
        </section>
        <section class="card stat-card">
          <p>Special Offers</p>
          <h2 id="stat-offers">0</h2>
        </section>
        <section class="card stat-card">
          <p>Newsletter Subscribers</p>
          <h2 id="stat-newsletter">0</h2>
        </section>
      </div>

      <section id="home-section" class="home-section">
        <div class="home-panels">
          <article class="card home-card">
            <div class="panel-heading">
              <div>
                <h3>Recent Activity</h3>
                <p class="panel-note">Changes, submissions and email events tracked live.</p>
              </div>
              <span class="badge status-info">Live</span>
            </div>
            <ul id="recent-activity" class="activity-list">
              <li class="activity-item empty">No recent activity yet.</li>
            </ul>
          </article>
          <article class="card home-card">
            <div class="panel-heading">
              <div>
                <h3>Quick Actions</h3>
                <p class="panel-note">Jump directly into the most-used workflows.</p>
              </div>
              <span class="badge status-success">Fast</span>
            </div>
            <div class="quick-actions">
              <button type="button" class="btn-main quick-action" data-action="bookings">Add Booking</button>
              <button type="button" class="btn-main quick-action" data-action="appointments">Add Appointment</button>
              <button type="button" class="btn-main quick-action" data-action="visa_applications">Add Visa Request</button>
              <button type="button" class="btn-main quick-action" data-action="study_applications">Add Study Application</button>
              <button type="button" class="btn-main quick-action" data-action="blogs">New Blog Post</button>
              <button type="button" class="btn-main quick-action" data-action="gallery">Upload Gallery Image</button>
              <button type="button" class="btn-main quick-action" data-action="testimonials">Add Testimonial</button>
              <button type="button" class="btn-main quick-action" data-action="special_offers">Add Special Offer</button>
            </div>
          </article>
        </div>
      </section>

      <section class="dashboard-toolbar" aria-label="Table controls">
        <div class="toolbar-left">
          <label class="screen-reader-text" for="search-input">Search records</label>
          <input id="search-input" class="form-control" type="search" placeholder="Search name, email, phone, or status">
        </div>
        <div class="toolbar-center">
          <label class="screen-reader-text" for="sort-field">Sort records</label>
          <select id="sort-field" class="form-control" aria-label="Sort records">
            <option value="">Sort by</option>
          </select>
          <button id="sort-toggle" type="button" class="btn-secondary" title="Toggle sort direction"><i class="fa-solid fa-arrow-up-wide-short"></i></button>
          <label class="screen-reader-text" for="status-filter">Filter by status</label>
          <select id="status-filter" class="form-control" aria-label="Filter records by status">
            <option value="">All Status</option>
          </select>
        </div>
        <div class="toolbar-action">
          <button id="export-csv" class="btn-main" type="button"><i class="fa-solid fa-file-csv"></i>Export CSV</button>
          <button id="print-view" class="btn-main" type="button"><i class="fa-solid fa-print"></i>Print</button>
          <button id="module-action-button" class="btn-main hidden" type="button"><i class="fa-solid fa-plus"></i>Action</button>
        </div>
      </section>

      <section id="table-section" class="table-section hidden" aria-label="Module records">
        <div class="table-wrapper">
          <table id="data-table">
            <thead>
              <tr id="table-head"></tr>
            </thead>
            <tbody id="table-body"></tbody>
          </table>
        </div>
        <div class="pagination hidden" id="pagination-bar" aria-label="Table pagination">
          <button id="previous-page" type="button" class="btn-secondary">Previous</button>
          <span id="page-indicator" class="page-indicator">Page 1</span>
          <button id="next-page" type="button" class="btn-secondary">Next</button>
        </div>
      </section>
    </main>
  </div>

  <div id="toast-container" class="toast-container" aria-live="polite" aria-atomic="true"></div>

  <div id="record-modal" class="modal-backdrop hidden" role="dialog" aria-modal="true" aria-labelledby="modal-title">
    <div class="modal">
      <div class="modal-header">
        <h2 id="modal-title">Record details</h2>
        <button id="modal-close" class="modal-close" aria-label="Close modal">×</button>
      </div>
      <div class="modal-body" id="modal-body"></div>
      <div class="modal-footer" id="modal-footer"></div>
    </div>
  </div>

  <script type="module" src="../js/dashboard.js"></script>
</body>
</html>
'''

css = '''/* ==========================================
   SUI-GENERIS ADMIN DASHBOARD
========================================== */
:root {
  --primary: #f58220;
  --primary-dark: #d96c10;
  --navy: #0f172a;
  --surface: #ffffff;
  --bg: #f4f7fb;
  --text: #111827;
  --text-muted: #475569;
  --muted: #64748b;
  --border: #e5e7eb;
  --shadow: 0 18px 48px rgba(15, 23, 42, 0.12);
  --radius: 20px;
  --transition: 0.22s ease;
}
* {
  box-sizing: border-box;
}
html {
  scroll-behavior: smooth;
}
body {
  margin: 0;
  font-family: Inter, "Segoe UI", Arial, sans-serif;
  background: var(--bg);
  color: var(--text);
}
button,
select,
input {
  font: inherit;
}
button {
  cursor: pointer;
}
button:disabled,
input:disabled,
select:disabled {
  cursor: not-allowed;
  opacity: 0.6;
}
.screen-reader-text {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}
.admin-layout {
  display: grid;
  grid-template-columns: 280px 1fr;
  min-height: 100vh;
}
.sidebar {
  background: var(--navy);
  color: white;
  display: flex;
  flex-direction: column;
  padding: 32px 24px;
  position: sticky;
  top: 0;
  height: 100vh;
}
.sidebar-brand {
  display: flex;
  align-items: center;
  gap: 14px;
  margin-bottom: 40px;
}
.sidebar-brand img {
  width: 52px;
  height: 52px;
  object-fit: cover;
  border-radius: 16px;
  background: white;
}
.sidebar-brand span {
  font-size: 1rem;
  font-weight: 700;
  letter-spacing: 0.02em;
}
.sidebar-brand p {
  margin: 4px 0 0;
  font-size: 0.85rem;
  color: #cbd5e1;
}
.sidebar-nav {
  display: flex;
  flex-direction: column;
  gap: 10px;
  flex: 1;
}
.nav-item {
  display: flex;
  align-items: center;
  gap: 12px;
  width: 100%;
  padding: 14px 16px;
  border-radius: 14px;
  border: none;
  background: transparent;
  color: #cbd5e1;
  text-align: left;
  transition: background var(--transition), transform var(--transition), color var(--transition);
}
.nav-item:hover,
.nav-item:focus-visible {
  background: rgba(255, 255, 255, 0.08);
  color: white;
  outline: none;
}
.nav-item.active {
  background: rgba(245, 130, 32, 0.16);
  color: white;
  box-shadow: 0 18px 30px rgba(245, 130, 32, 0.14);
}
.nav-item i {
  width: 18px;
  text-align: center;
}
.nav-signout {
  margin-top: 18px;
  color: #fecaca;
  justify-content: flex-start;
}
.main-content {
  padding: 32px 34px;
}
.top-header {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  gap: 20px;
  margin-bottom: 28px;
}
.top-header h1 {
  margin: 0;
  font-size: clamp(2rem, 3vw, 2.8rem);
  font-weight: 800;
  line-height: 1.05;
}
.top-header p {
  margin: 10px 0 0;
  color: var(--muted);
  max-width: 720px;
}
.stats-grid {
  display: grid;
  grid-template-columns: repeat(4, minmax(180px, 1fr));
  gap: 18px;
  margin-bottom: 30px;
}
.stat-card {
  background: white;
  border-radius: var(--radius);
  padding: 24px;
  border: 1px solid rgba(226, 232, 240, 0.85);
  box-shadow: 0 16px 34px rgba(15, 23, 42, 0.08);
}
.stat-card p {
  margin: 0;
  color: var(--muted);
  font-size: 0.9rem;
}
.stat-card h2 {
  margin: 14px 0 0;
  font-size: 2rem;
  color: var(--primary-dark);
}
.home-section {
  margin-bottom: 28px;
}
.home-panels {
  display: grid;
  grid-template-columns: 1.2fr 0.8fr;
  gap: 18px;
}
.home-card {
  padding: 24px;
  min-height: 280px;
}
.panel-heading {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 16px;
  margin-bottom: 18px;
}
.panel-heading h3 {
  margin: 0;
  font-size: 1.05rem;
}
.panel-note {
  margin: 6px 0 0;
  color: var(--muted);
  font-size: 0.9rem;
}
.badge {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 8px 14px;
  border-radius: 999px;
  font-size: 0.8rem;
  font-weight: 700;
}
.status-info {
  background: #dbeafe;
  color: #1d4ed8;
}
.status-success {
  background: #dcfce7;
  color: #166534;
}
.activity-list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 12px;
}
.activity-item {
  padding: 16px;
  border-radius: 16px;
  border: 1px solid rgba(226, 232, 240, 0.8);
  background: #fbfdff;
  color: var(--text-muted);
}
.activity-item.empty {
  font-style: italic;
}
.quick-actions {
  display: grid;
  grid-template-columns: repeat(2, minmax(150px, 1fr));
  gap: 14px;
}
.dashboard-toolbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 14px;
  margin-bottom: 24px;
  flex-wrap: nowrap;
}
.dashboard-toolbar input,
.dashboard-toolbar select {
  width: 100%;
  min-height: 46px;
  padding: 13px 14px;
  border-radius: 14px;
  border: 1px solid var(--border);
  background: white;
  color: var(--text);
  transition: border-color var(--transition), box-shadow var(--transition);
}
.dashboard-toolbar input:focus,
.dashboard-toolbar select:focus {
  outline: none;
  border-color: var(--primary-dark);
  box-shadow: 0 0 0 4px rgba(245, 130, 32, 0.12);
}
.toolbar-left {
  flex: 0 0 320px;
}
.toolbar-left input {
  width: 100%;
}
.toolbar-center {
  display: flex;
  gap: 0.9rem;
  flex: 1 1 0;
  min-width: 0;
  align-items: center;
}
#sort-field {
  flex: 1 1 0;
  min-width: 0;
}
#status-filter {
  width: 200px;
  min-width: 140px;
}
.toolbar-action {
  display: flex;
  flex-wrap: wrap;
  gap: 0.85rem;
  align-items: center;
  justify-content: flex-end;
  flex: 0 0 auto;
}
.btn-main,
.btn-secondary,
.btn-ghost {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  border: none;
  border-radius: 14px;
  padding: 12px 18px;
  font-weight: 700;
  transition: transform var(--transition), background var(--transition), box-shadow var(--transition), border-color var(--transition);
}
.btn-main {
  background: var(--primary);
  color: white;
  box-shadow: 0 16px 28px rgba(245, 130, 32, 0.2);
}
.btn-main:hover:not(:disabled) {
  transform: translateY(-1px);
  background: #e3751c;
}
.btn-main:active:not(:disabled) {
  transform: translateY(0);
}
.btn-secondary {
  background: #f8fafc;
  color: var(--text);
  border: 1px solid var(--border);
}
.btn-secondary:hover:not(:disabled) {
  transform: translateY(-1px);
  background: #eff4fb;
}
.btn-secondary:active:not(:disabled) {
  transform: translateY(0);
}
.btn-ghost {
  background: transparent;
  color: var(--text);
  border: 1px solid rgba(15, 23, 42, 0.12);
}
.btn-ghost:hover:not(:disabled) {
  background: rgba(15, 23, 42, 0.04);
}
.btn-main.hidden {
  display: none !important;
}
.table-section {
  margin-top: 8px;
}
.table-wrapper {
  background: white;
  border-radius: 24px;
  overflow: auto;
  border: 1px solid rgba(226, 232, 240, 0.95);
  box-shadow: 0 18px 36px rgba(15, 23, 42, 0.08);
}
table {
  width: 100%;
  min-width: 760px;
  border-collapse: collapse;
}
thead {
  background: #f8fafc;
}
th,
td {
  padding: 18px 16px;
  text-align: left;
  vertical-align: middle;
}
th {
  color: #64748b;
  font-size: 0.85rem;
  font-weight: 700;
  letter-spacing: 0.02em;
}
th.sortable {
  cursor: pointer;
}
th.sortable:hover {
  color: var(--primary-dark);
}
tbody tr {
  transition: background var(--transition);
}
tbody tr:hover {
  background: #f8fafc;
}
td {
  border-top: 1px solid rgba(226, 232, 240, 0.95);
  color: var(--text);
  font-size: 0.95rem;
}
.actions {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
}
.btn-view,
.btn-edit,
.btn-delete,
.btn-print {
  width: 42px;
  height: 42px;
  border-radius: 12px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border: none;
  transition: transform var(--transition), box-shadow var(--transition), background var(--transition);
}
.btn-view {
  background: #dbeafe;
  color: #1d4ed8;
}
.btn-edit {
  background: #fde68a;
  color: #92400e;
}
.btn-delete {
  background: #fee2e2;
  color: #b91c1c;
}
.btn-print {
  background: #d1fae5;
  color: #166534;
}
.btn-view:hover,
.btn-edit:hover,
.btn-delete:hover,
.btn-print:hover {
  transform: scale(1.05);
}
.badge-pill {
  display: inline-flex;
  align-items: center;
  padding: 8px 12px;
  border-radius: 999px;
  font-size: 0.8rem;
  font-weight: 700;
}
.badge-pill.pending {
  background: #fef3c7;
  color: #92400e;
}
.badge-pill.processing {
  background: #dbeafe;
  color: #1d4ed8;
}
.badge-pill.confirmed,
.badge-pill.completed {
  background: #dcfce7;
  color: #166534;
}
.badge-pill.cancelled {
  background: #fee2e2;
  color: #b91c1c;
}
.badge-pill.true {
  background: #dcfce7;
  color: #166534;
}
.badge-pill.false {
  background: #f8fafc;
  color: #475569;
}
.pagination {
  display: flex;
  align-items: center;
  justify-content: flex-end;
  gap: 14px;
  margin-top: 18px;
}
.page-indicator {
  color: var(--muted);
}
.pagination button {
  min-width: 112px;
}
.empty-state td,
.loading-row td {
  text-align: center;
  color: var(--muted);
  padding: 3rem 1rem;
}
.skeleton-row td {
  padding: 18px;
}
.skeleton-line {
  height: 12px;
  border-radius: 999px;
  background: linear-gradient(90deg, rgba(229, 241, 255, 0.85), rgba(243, 243, 243, 1), rgba(229, 241, 255, 0.85));
  background-size: 200% 100%;
  animation: shimmer 1.6s infinite ease-in-out;
}
@keyframes shimmer {
  0% { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}
.toast-container {
  position: fixed;
  bottom: 24px;
  right: 24px;
  display: flex;
  flex-direction: column;
  gap: 12px;
  z-index: 1100;
  pointer-events: none;
}
.toast {
  pointer-events: auto;
  min-width: 280px;
  max-width: 360px;
  padding: 16px 18px;
  border-radius: 16px;
  box-shadow: 0 18px 40px rgba(15, 23, 42, 0.2);
  color: white;
  display: inline-flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  animation: pop-in 0.25s ease;
}
.toast.success { background: #16a34a; }
.toast.error { background: #dc2626; }
.toast.info { background: #2563eb; }
@keyframes pop-in {
  from { opacity: 0; transform: translateX(18px); }
  to { opacity: 1; transform: translateX(0); }
}
.modal-backdrop {
  position: fixed;
  inset: 0;
  background: rgba(15, 23, 42, 0.55);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px;
  z-index: 1200;
}
.modal-backdrop.hidden {
  display: none;
}
.modal {
  width: min(760px, 100%);
  background: white;
  border-radius: 26px;
  box-shadow: 0 30px 60px rgba(15, 23, 42, 0.18);
  overflow: hidden;
}
.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 16px;
  padding: 22px 22px 18px;
  border-bottom: 1px solid rgba(226, 232, 240, 0.95);
}
.modal-header h2 {
  margin: 0;
  font-size: 1.2rem;
}
.modal-close {
  border: none;
  background: transparent;
  color: var(--text-muted);
  font-size: 1.7rem;
}
.modal-body {
  padding: 22px;
}
.modal-body dl {
  display: grid;
  grid-template-columns: minmax(160px, 1fr) 1.5fr;
  gap: 12px 18px;
}
.modal-body dt {
  margin: 0;
  font-weight: 700;
  color: #334155;
}
.modal-body dd {
  margin: 0;
  color: #475569;
  white-space: pre-wrap;
}
.modal-footer {
  display: flex;
  justify-content: flex-end;
  gap: 12px;
  align-items: center;
  padding: 18px 22px 22px;
  border-top: 1px solid rgba(226, 232, 240, 0.95);
}
.modal-footer button {
  min-width: 110px;
}
.hidden {
  display: none !important;
}
@media (max-width: 1200px) {
  .stats-grid {
    grid-template-columns: repeat(2, minmax(180px, 1fr));
  }
}
@media (max-width: 992px) {
  .admin-layout {
    grid-template-columns: 1fr;
  }
  .sidebar {
    position: relative;
    height: auto;
  }
  .main-content {
    padding: 24px;
  }
  .dashboard-toolbar {
    flex-wrap: wrap;
    justify-content: stretch;
  }
  .toolbar-left,
  .toolbar-center,
  .toolbar-action {
    width: 100%;
  }
  .toolbar-center {
    flex-wrap: wrap;
  }
  #status-filter {
    width: 100%;
  }
}
@media (max-width: 768px) {
  .home-panels {
    grid-template-columns: 1fr;
  }
  .quick-actions {
    grid-template-columns: 1fr;
  }
  .dashboard-toolbar {
    gap: 12px;
  }
  .table-wrapper {
    overflow-x: auto;
  }
  table {
    min-width: 660px;
  }
  .modal-body dl {
    grid-template-columns: 1fr;
  }
}
@media (max-width: 640px) {
  .sidebar {
    padding: 24px 18px;
  }
  .main-content {
    padding: 18px;
  }
  .btn-main,
  .btn-secondary {
    width: 100%;
    justify-content: center;
  }
}
'''

js = '''import { supabase } from "./supabase.js";

const sessionResult = await supabase.auth.getSession();
if (!sessionResult?.data?.session) {
  window.location.href = "../admin/login.html";
}

const MODULES = {
  home: {
    title: "Dashboard Home",
    description: "Overview of your travel operations, live status, and quick actions.",
    isHome: true
  },
  bookings: {
    title: "Flight Bookings",
    table: "bookings",
    countId: "stat-bookings",
    columns: ["fullname", "phone", "departure_city", "destination_city", "departure_date", "status"],
    searchFields: ["fullname", "phone", "departure_city", "destination_city", "status"],
    sortFields: [
      { value: "departure_date", label: "Departure Date" },
      { value: "destination_city", label: "Destination" },
      { value: "fullname", label: "Customer" },
      { value: "status", label: "Status" }
    ],
    statusField: "status",
    statusOptions: [
      { value: "", label: "All Status" },
      { value: "pending", label: "Pending" },
      { value: "processing", label: "Processing" },
      { value: "confirmed", label: "Confirmed" },
      { value: "completed", label: "Completed" },
      { value: "cancelled", label: "Cancelled" }
    ],
    detailFields: ["fullname", "email", "phone", "departure_city", "destination_city", "departure_date", "return_date", "passenger_count", "class", "status", "notes", "created_at"]
  },
  visa_applications: {
    title: "Visa Applications",
    table: "visa_applications",
    countId: "stat-visas",
    columns: ["fullname", "country", "visa_type", "travel_date", "status"],
    searchFields: ["fullname", "country", "visa_type", "status"],
    sortFields: [
      { value: "country", label: "Country" },
      { value: "visa_type", label: "Visa Type" },
      { value: "travel_date", label: "Travel Date" },
      { value: "status", label: "Status" }
    ],
    statusField: "status",
    statusOptions: [
      { value: "", label: "All Status" },
      { value: "new", label: "New" },
      { value: "processing", label: "Processing" },
      { value: "confirmed", label: "Confirmed" },
      { value: "completed", label: "Completed" },
      { value: "cancelled", label: "Cancelled" }
    ],
    detailFields: ["fullname", "email", "phone", "country", "visa_type", "travel_date", "passport_number", "nationality", "status", "notes", "created_at"]
  },
  study_applications: {
    title: "Study Abroad Applications",
    table: "study_applications",
    countId: "stat-study",
    columns: ["fullname", "country", "course", "qualification", "status"],
    searchFields: ["fullname", "country", "course", "qualification", "status"],
    sortFields: [
      { value: "country", label: "Country" },
      { value: "institution", label: "Institution" },
      { value: "course", label: "Course" },
      { value: "qualification", label: "Qualification" },
      { value: "status", label: "Status" }
    ],
    statusField: "status",
    statusOptions: [
      { value: "", label: "All Status" },
      { value: "pending", label: "Pending" },
      { value: "processing", label: "Processing" },
      { value: "confirmed", label: "Confirmed" },
      { value: "completed", label: "Completed" },
      { value: "cancelled", label: "Cancelled" }
    ],
    detailFields: ["fullname", "email", "phone", "country", "institution", "course", "qualification", "status", "notes", "created_at"]
  },
  appointments: {
    title: "Appointments",
    table: "appointments",
    countId: "stat-appointments",
    columns: ["fullname", "service", "appointment_date", "status"],
    searchFields: ["fullname", "service", "status"],
    sortFields: [
      { value: "appointment_date", label: "Appointment Date" },
      { value: "status", label: "Status" },
      { value: "fullname", label: "Customer" }
    ],
    statusField: "status",
    statusOptions: [
      { value: "", label: "All Status" },
      { value: "pending", label: "Pending" },
      { value: "confirmed", label: "Confirmed" },
      { value: "completed", label: "Completed" },
      { value: "cancelled", label: "Cancelled" }
    ],
    detailFields: ["fullname", "email", "phone", "service", "appointment_date", "appointment_time", "status", "notes", "created_at"]
  },
  contacts: {
    title: "Customer Inquiries",
    table: "contacts",
    countId: "stat-contacts",
    columns: ["fullname", "email", "phone", "subject", "status", "created_at"],
    searchFields: ["fullname", "email", "phone", "subject", "message"],
    sortFields: [
      { value: "created_at", label: "Date" },
      { value: "fullname", label: "Sender" },
      { value: "subject", label: "Subject" }
    ],
    statusField: "status",
    statusOptions: [
      { value: "", label: "All Status" },
      { value: "new", label: "New" },
      { value: "read", label: "Read" },
      { value: "replied", label: "Replied" },
      { value: "closed", label: "Closed" }
    ],
    archiveStatus: "closed",
    detailFields: ["fullname", "email", "phone", "subject", "message", "status", "created_at"]
  },
  blogs: {
    title: "Blog Manager",
    table: "blogs",
    countId: "stat-blogs",
    columns: ["title", "category", "published", "featured", "created_at"],
    searchFields: ["title", "excerpt", "content", "category", "author"],
    sortFields: [
      { value: "created_at", label: "Newest" },
      { value: "title", label: "Title" },
      { value: "category", label: "Category" },
      { value: "published", label: "Published" }
    ],
    statusField: "published",
    statusOptions: [
      { value: "", label: "All Posts" },
      { value: "true", label: "Published" },
      { value: "false", label: "Draft" }
    ],
    detailFields: ["title", "author", "category", "published", "featured", "views", "created_at"]
  },
  gallery: {
    title: "Gallery Manager",
    table: "gallery",
    countId: "stat-gallery",
    columns: ["title", "category", "featured", "created_at"],
    searchFields: ["title", "category", "description"],
    sortFields: [
      { value: "created_at", label: "Newest" },
      { value: "title", label: "Title" },
      { value: "category", label: "Category" },
      { value: "featured", label: "Featured" }
    ],
    statusField: "featured",
    statusOptions: [
      { value: "", label: "All Items" },
      { value: "true", label: "Featured" },
      { value: "false", label: "Standard" }
    ],
    detailFields: ["title", "category", "description", "featured", "display_order", "created_at"]
  },
  testimonials: {
    title: "Testimonials",
    table: "testimonials",
    countId: "stat-testimonials",
    columns: ["name", "country", "rating", "approved", "created_at"],
    searchFields: ["name", "country", "message"],
    sortFields: [
      { value: "created_at", label: "Newest" },
      { value: "name", label: "Name" },
      { value: "rating", label: "Rating" },
      { value: "approved", label: "Approved" }
    ],
    statusField: "approved",
    statusOptions: [
      { value: "", label: "All Reviews" },
      { value: "true", label: "Approved" },
      { value: "false", label: "Pending" }
    ],
    detailFields: ["name", "country", "rating", "message", "approved", "created_at"]
  },
  special_offers: {
    title: "Special Offers",
    table: "special_offers",
    countId: "stat-offers",
    columns: ["title", "discount_label", "start_date", "end_date", "active"],
    searchFields: ["title", "description", "discount_label"],
    sortFields: [
      { value: "start_date", label: "Start Date" },
      { value: "end_date", label: "End Date" },
      { value: "title", label: "Title" },
      { value: "active", label: "Active" }
    ],
    statusField: "active",
    statusOptions: [
      { value: "", label: "All Offers" },
      { value: "true", label: "Active" },
      { value: "false", label: "Paused" }
    ],
    detailFields: ["title", "description", "discount_label", "start_date", "end_date", "active", "created_at"]
  },
  newsletter: {
    title: "Newsletter Subscribers",
    table: "newsletter",
    countId: "stat-newsletter",
    columns: ["email", "active", "created_at"],
    searchFields: ["email"],
    sortFields: [
      { value: "created_at", label: "Newest" },
      { value: "email", label: "Email" },
      { value: "active", label: "Active" }
    ],
    statusField: "active",
    statusOptions: [
      { value: "", label: "All Subscribers" },
      { value: "true", label: "Active" },
      { value: "false", label: "Inactive" }
    ],
    detailFields: ["email", "active", "created_at"]
  }
};

const state = {
  module: "home",
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
  pages: 1,
  activity: [],
  modalRecord: null,
  modalConfig: null
};

const elements = {
  navItems: document.querySelectorAll(".nav-item[data-table]"),
  quickActions: document.querySelectorAll(".quick-action"),
  searchInput: document.getElementById("search-input"),
  sortFieldSelect: document.getElementById("sort-field"),
  sortToggleBtn: document.getElementById("sort-toggle"),
  statusFilterSelect: document.getElementById("status-filter"),
  exportCsvBtn: document.getElementById("export-csv"),
  printViewBtn: document.getElementById("print-view"),
  moduleActionButton: document.getElementById("module-action-button"),
  previousPageBtn: document.getElementById("previous-page"),
  nextPageBtn: document.getElementById("next-page"),
  pageIndicator: document.getElementById("page-indicator"),
  paginationBar: document.getElementById("pagination-bar"),
  tableSection: document.getElementById("table-section"),
  homeSection: document.getElementById("home-section"),
  pageTitle: document.getElementById("page-title"),
  pageDescription: document.getElementById("page-description"),
  toastContainer: document.getElementById("toast-container"),
  modalBackdrop: document.getElementById("record-modal"),
  modalBody: document.getElementById("modal-body"),
  modalFooter: document.getElementById("modal-footer"),
  modalClose: document.getElementById("modal-close")
};

function getConfig(moduleName) {
  return MODULES[moduleName] ?? null;
}

function setActiveNav(moduleName) {
  elements.navItems.forEach(item => {
    item.classList.toggle("active", item.dataset.table === moduleName);
  });
}

function updateHeader(config) {
  if (elements.pageTitle) elements.pageTitle.textContent = config.title;
  if (elements.pageDescription) elements.pageDescription.textContent = config.description || "Manage records and streamline operations.";
}

function resetFilters() {
  state.searchTerm = "";
  state.statusFilter = "";
  state.sortField = "";
  state.sortAscending = true;
  if (elements.searchInput) elements.searchInput.value = "";
  if (elements.statusFilterSelect) elements.statusFilterSelect.value = "";
  if (elements.sortFieldSelect) elements.sortFieldSelect.value = "";
}

function showHomeView() {
  elements.homeSection?.classList.remove("hidden");
  elements.tableSection?.classList.add("hidden");
  elements.paginationBar?.classList.add("hidden");
}

function showTableView() {
  elements.homeSection?.classList.add("hidden");
  elements.tableSection?.classList.remove("hidden");
  elements.paginationBar?.classList.remove("hidden");
}

function setLoading(isLoading) {
  state.loading = isLoading;
  if (state.module !== "home") {
    renderTable(getConfig(state.module), []);
  }
}

function formatHeading(key) {
  return String(key)
    .replace(/_/g, " ")
    .replace(/\b\w/g, char => char.toUpperCase());
}

function formatDate(value) {
  if (value === null || value === undefined || value === "") return "-";
  const date = new Date(value);
  if (Number.isNaN(date.getTime())) return String(value);
  return date.toLocaleDateString(undefined, { year: "numeric", month: "short", day: "numeric" });
}

function getRecordById(recordId) {
  return state.records.find(record => String(record.id) === String(recordId)) ?? null;
}

function renderRecentActivity() {
  const list = document.getElementById("recent-activity");
  if (!list) return;
  if (!state.activity.length) {
    list.innerHTML = '<li class="activity-item empty">No recent activity yet.</li>';
    return;
  }
  list.innerHTML = state.activity.map(entry => `
    <li class="activity-item">
      <strong>${entry.message}</strong><br>
      <small>${entry.time}</small>
    </li>
  `).join("");
}

function addRecentActivity(message) {
  state.activity.unshift({ message, time: new Date().toLocaleString() });
  if (state.activity.length > 8) state.activity.pop();
  renderRecentActivity();
}

function applyToolbar(config) {
  if (!elements.sortFieldSelect || !elements.statusFilterSelect || !elements.moduleActionButton) return;
  const sortOptions = config.sortFields ?? [];
  elements.sortFieldSelect.innerHTML = `<option value="">Sort by</option>${sortOptions.map(field => `<option value="${field.value}">${field.label}</option>`).join("")}`;
  elements.sortFieldSelect.disabled = sortOptions.length === 0;
  elements.sortToggleBtn.disabled = sortOptions.length === 0;
  const statusOptions = config.statusOptions ?? [{ value: "", label: "All Status" }];
  elements.statusFilterSelect.innerHTML = statusOptions.map(option => `<option value="${option.value}">${option.label}</option>`).join("");
  elements.statusFilterSelect.disabled = !config.statusField;
  if (config.isHome) {
    elements.moduleActionButton.classList.add("hidden");
  } else {
    elements.moduleActionButton.classList.remove("hidden");
    const actionName = config.title.replace(/s$/, "");
    elements.moduleActionButton.innerHTML = `<i class="fa-solid fa-plus"></i>New ${actionName}`;
  }
}

async function loadDashboardStats() {
  await Promise.all(Object.values(MODULES).map(async config => {
    if (!config.table || !config.countId) return;
    try {
      const { count, error } = await supabase.from(config.table).select("*", { count: "exact", head: true });
      if (error) throw error;
      const element = document.getElementById(config.countId);
      if (element) element.textContent = String(count ?? 0);
    } catch (error) {
      console.warn("Dashboard stat error:", error);
    }
  }));
}

function updatePagination() {
  if (!elements.pageIndicator || !elements.previousPageBtn || !elements.nextPageBtn) return;
  elements.pageIndicator.textContent = `Page ${state.currentPage} of ${state.pages} · ${state.totalCount} record${state.totalCount === 1 ? "" : "s"}`;
  elements.previousPageBtn.disabled = state.currentPage <= 1;
  elements.nextPageBtn.disabled = state.currentPage >= state.pages;
}

function normalizeValue(value) {
  if (value === null || value === undefined) return "";
  return String(value).toLowerCase();
}

function applyFiltersAndRender() {
  const config = getConfig(state.module);
  if (!config) {
    showToast("Module configuration is missing.", "error");
    return;
  }
  if (config.isHome) {
    renderHome();
    return;
  }
  let records = [...state.records];
  if (state.statusFilter && config.statusField) {
    records = records.filter(record => normalizeValue(record[config.statusField]) === normalizeValue(state.statusFilter));
  }
  if (state.searchTerm) {
    const query = state.searchTerm.toLowerCase();
    records = records.filter(record => config.searchFields.some(field => normalizeValue(record[field]).includes(query)));
  }
  if (state.sortField) {
    records.sort((a, b) => {
      const aValue = normalizeValue(a[state.sortField]);
      const bValue = normalizeValue(b[state.sortField]);
      if (!aValue && bValue) return state.sortAscending ? -1 : 1;
      if (aValue && !bValue) return state.sortAscending ? 1 : -1;
      if (aValue === bValue) return 0;
      return state.sortAscending ? aValue.localeCompare(bValue, undefined, { numeric: true, sensitivity: "base" }) : bValue.localeCompare(aValue, undefined, { numeric: true, sensitivity: "base" });
    });
  }
  state.filteredRecords = records;
  state.totalCount = records.length;
  state.pages = Math.max(1, Math.ceil(records.length / state.pageSize));
  if (state.currentPage > state.pages) state.currentPage = state.pages;
  const start = (state.currentPage - 1) * state.pageSize;
  const pageData = records.slice(start, start + state.pageSize);
  renderTable(config, pageData);
  updatePagination();
}

function renderTable(config, data) {
  const head = document.getElementById("table-head");
  const body = document.getElementById("table-body");
  if (!head || !body) return;
  head.innerHTML = "";
  body.innerHTML = "";
  const columns = config.columns || [];
  columns.forEach(col => {
    const sortable = config.sortFields?.some(field => field.value === col);
    head.innerHTML += `<th class="${sortable ? "sortable" : ""}" data-key="${col}">${formatHeading(col)}</th>`;
  });
  head.innerHTML += `<th>Actions</th>`;
  if (state.loading) {
    body.innerHTML = Array.from({ length: 4 }).map(() => `
      <tr class="skeleton-row">
        ${columns.map(() => `<td><div class="skeleton-line"></div></td>`).join("")}<td><div class="skeleton-line"></div></td>
      </tr>`).join("");
    return;
  }
  if (!data.length) {
    body.innerHTML = `<tr class="empty-state"><td colspan="${columns.length + 1}">No records found for this view. Adjust search, filters, or choose another module.</td></tr>`;
    return;
  }
  body.innerHTML = data.map(record => {
    const cells = columns.map(col => {
      const rawValue = record[col];
      if (col === config.statusField) {
        const options = (config.statusOptions || []).map(option => `<option value="${option.value}" ${String(rawValue) === String(option.value) ? "selected" : ""}>${option.label}</option>`).join("");
        return `<td><select class="record-status form-control" data-id="${record.id}" aria-label="Update status for ${record.fullname || "item"}">${options}</select></td>`;
      }
      if (typeof rawValue === "boolean") {
        return `<td><span class="badge-pill ${rawValue}">${rawValue ? "Yes" : "No"}</span></td>`;
      }
      if (col.endsWith("_date") || col.endsWith("_at")) {
        return `<td>${formatDate(rawValue)}</td>`;
      }
      const displayed = String(rawValue ?? "-");
      return `<td>${displayed.length > 70 ? `${displayed.slice(0, 70)}…` : displayed}</td>`;
    }).join("");
    return `
      <tr>
        ${cells}
        <td class="actions">
          <button type="button" class="btn-view" data-id="${record.id}" aria-label="View record"><i class="fa-solid fa-eye"></i></button>
          <button type="button" class="btn-edit" data-id="${record.id}" aria-label="Edit record"><i class="fa-solid fa-pen"></i></button>
          <button type="button" class="btn-print" data-id="${record.id}" aria-label="Print record"><i class="fa-solid fa-print"></i></button>
          <button type="button" class="btn-delete" data-id="${record.id}" aria-label="Delete record"><i class="fa-solid fa-trash"></i></button>
        </td>
      </tr>`;
  }).join("");
}

async function loadModule(moduleName) {
  const config = getConfig(moduleName);
  if (!config) {
    showToast("Module not found.", "error");
    return;
  }
  setActiveNav(moduleName);
  state.module = moduleName;
  resetFilters();
  updateHeader(config);
  applyToolbar(config);
  if (config.isHome) {
    showHomeView();
    renderRecentActivity();
    return;
  }
  showTableView();
  state.currentPage = 1;
  state.searchTerm = "";
  state.statusFilter = "";
  state.sortField = "";
  state.sortAscending = true;
  setLoading(true);
  if (!config.table) {
    setLoading(false);
    showToast("No table configured for this module.", "error");
    return;
  }
  const { data, error } = await supabase.from(config.table).select("*").order("created_at", { ascending: false });
  setLoading(false);
  if (error) {
    console.error(error);
    showToast(`Unable to load ${config.title}.`, "error");
    state.records = [];
    applyFiltersAndRender();
    return;
  }
  state.records = data ?? [];
  applyFiltersAndRender();
  addRecentActivity(`Opened ${config.title}`);
}

function handleSearch(event) {
  state.searchTerm = event.target.value.trim();
  state.currentPage = 1;
  applyFiltersAndRender();
}

function handleFilter(event) {
  state.statusFilter = event.target.value;
  state.currentPage = 1;
  applyFiltersAndRender();
}

function handleSort(event) {
  state.sortField = event.target.value;
  state.currentPage = 1;
  applyFiltersAndRender();
}

function handleSortToggle() {
  state.sortAscending = !state.sortAscending;
  applyFiltersAndRender();
}

function handlePageChange(step) {
  state.currentPage = Math.min(state.pages, Math.max(1, state.currentPage + step));
  applyFiltersAndRender();
}

function renderHome() {
  showHomeView();
  loadDashboardStats();
}

function openModal(record, config, mode = "view") {
  if (!elements.modalBackdrop || !elements.modalBody || !elements.modalFooter) return;
  const details = (config.detailFields || Object.keys(record || {})).map(key => `
    <dt>${formatHeading(key)}</dt><dd>${formatFieldValue(key, record[key])}</dd>`).join("");
  elements.modalBody.innerHTML = `<dl>${details}</dl>`;
  elements.modalFooter.innerHTML = `
    <button type="button" class="btn-secondary" id="modal-cancel">Cancel</button>
    <button type="button" class="btn-main" id="modal-save">Save</button>
    <button type="button" class="btn-ghost" id="modal-print">Print</button>
  `;
  elements.modalBackdrop.classList.remove("hidden");
  state.modalRecord = record;
  state.modalConfig = config;
}

function closeModal() {
  elements.modalBackdrop?.classList.add("hidden");
  if (elements.modalFooter) elements.modalFooter.innerHTML = "";
  state.modalRecord = null;
  state.modalConfig = null;
}

function formatFieldValue(key, value) {
  if (value === null || value === undefined || value === "") return "-";
  if (typeof value === "boolean") return value ? "Yes" : "No";
  if (key.endsWith("_date") || key.endsWith("_at")) return formatDate(value);
  return String(value).replace(/\n/g, "<br>");
}

async function updateStatus(recordId, value) {
  const config = getConfig(state.module);
  if (!config || !config.table || !config.statusField) return;
  const record = getRecordById(recordId);
  if (!record) return;
  const { error } = await supabase.from(config.table).update({ [config.statusField]: value }).eq("id", recordId);
  if (error) {
    showToast(error.message || "Unable to update status.", "error");
    applyFiltersAndRender();
    return;
  }
  record[config.statusField] = value;
  const filtered = state.filteredRecords.find(item => String(item.id) === String(recordId));
  if (filtered) filtered[config.statusField] = value;
  showToast("Status updated.", "success");
  addRecentActivity(`Updated ${config.title} status`);
}

async function deleteRecord(recordId) {
  const config = getConfig(state.module);
  if (!config || !config.table) return;
  if (!confirm(`Delete this ${config.title.replace(/s$/, "")} permanently?`)) return;
  const { error } = await supabase.from(config.table).delete().eq("id", recordId);
  if (error) {
    showToast(error.message || "Unable to delete record.", "error");
    return;
  }
  showToast("Record deleted.", "success");
  addRecentActivity(`Deleted ${config.title} record`);
  await loadModule(state.module);
}

function handleQuickAction(action) {
  const mapping = {
    bookings: "bookings",
    appointments: "appointments",
    visa_applications: "visa_applications",
    study_applications: "study_applications",
    blogs: "blogs",
    gallery: "gallery",
    testimonials: "testimonials",
    special_offers: "special_offers"
  };
  const moduleKey = mapping[action] || action;
  if (!MODULES[moduleKey]) {
    showToast("Action not configured.", "error");
    return;
  }
  loadModule(moduleKey);
}

function exportCurrentModuleCsv() {
  const config = getConfig(state.module);
  if (!config || config.isHome) {
    showToast("Select a module before exporting.", "error");
    return;
  }
  if (!state.filteredRecords.length) {
    showToast("No records to export.", "error");
    return;
  }
  const header = config.columns.map(formatHeading).join(",");
  const rows = state.filteredRecords.map(record => config.columns.map(col => escapeCsv(String(record[col] ?? ""))).join(",")).join("\n");
  const csv = `${header}\n${rows}`;
  const blob = new Blob([csv], { type: "text/csv;charset=utf-8;" });
  const url = URL.createObjectURL(blob);
  const anchor = document.createElement("a");
  anchor.href = url;
  anchor.download = `${config.table}-export-${new Date().toISOString().slice(0, 10)}.csv`;
  document.body.appendChild(anchor);
  anchor.click();
  anchor.remove();
  URL.revokeObjectURL(url);
  showToast("CSV export started.", "success");
}

function escapeCsv(value) {
  return value.includes(",") || value.includes("\n") || value.includes('"') ? `"${value.replace(/"/g, '""')}"` : value;
}

function openPrintWindow(content) {
  const printWindow = window.open("", "_blank", "width=900,height=700");
  if (!printWindow) {
    showToast("Unable to open print window.", "error");
    return;
  }
  printWindow.document.write(content);
  printWindow.document.close();
  printWindow.focus();
  printWindow.print();
}

function printCurrentView() {
  const config = getConfig(state.module);
  if (!config || config.isHome) {
    showToast("Select a module to print.", "error");
    return;
  }
  if (!state.filteredRecords.length) {
    showToast("No records to print.", "error");
    return;
  }
  const html = `
    <html>
      <head>
        <title>${config.title} Print</title>
        <style>body{font-family:Inter, sans-serif;color:#111827;padding:24px;}h1{font-size:24px;margin-bottom:16px;}table{width:100%;border-collapse:collapse;}th,td{padding:10px;border:1px solid #e5e7eb;text-align:left;}</style>
      </head>
      <body>
        <h1>${config.title}</h1>
        <table>
          <thead><tr>${config.columns.map(col => `<th>${formatHeading(col)}</th>`).join("")}</tr></thead>
          <tbody>${state.filteredRecords.map(record => `<tr>${config.columns.map(col => `<td>${sanitizePrintValue(record[col], col)}</td>`).join("")}</tr>`).join("")}</tbody>
        </table>
      </body>
    </html>`;
  openPrintWindow(html);
}

function sanitizePrintValue(value, key) {
  if (value === null || value === undefined) return "-";
  if (key.endsWith("_date") || key.endsWith("_at")) return formatDate(value);
  return String(value).replace(/\n/g, " ");
}

function handleModalAction(event) {
  const button = event.target.closest("button");
  if (!button || !button.id) return;
  if (button.id === "modal-cancel") {
    closeModal();
    return;
  }
  if (button.id === "modal-save") {
    showToast("Save functionality is ready to connect.", "info");
    return;
  }
  if (button.id === "modal-print") {
    if (!state.modalRecord || !state.modalConfig) return;
    printRecord(state.modalRecord, state.modalConfig);
    return;
  }
}

function printRecord(record, config) {
  const html = `
    <html>
      <head>
        <title>${config.title} Details</title>
        <style>body{font-family:Inter, sans-serif;color:#111827;padding:24px;}h1{font-size:24px;margin-bottom:18px;}dl{display:grid;grid-template-columns:200px 1fr;gap:12px 20px;}dt{font-weight:700;color:#334155;}dd{margin:0;color:#475569;}</style>
      </head>
      <body>
        <h1>${config.title}</h1>
        <dl>${(config.detailFields || Object.keys(record)).map(key => `<dt>${formatHeading(key)}</dt><dd>${sanitizePrintValue(record[key], key)}</dd>`).join("")}</dl>
      </body>
    </html>`;
  openPrintWindow(html);
}

function showToast(message, type = "info") {
  if (!elements.toastContainer) {
    console[type === "error" ? "error" : "log"](message);
    return;
  }
  const toast = document.createElement("div");
  toast.className = `toast ${type}`;
  toast.textContent = message;
  elements.toastContainer.appendChild(toast);
  setTimeout(() => toast.remove(), 4200);
}

function buildNotification(type, payload, recipient) {
  return {
    type,
    recipient,
    payload,
    createdAt: new Date().toISOString()
  };
}

function notifyBookingConfirmation(booking) {
  return buildNotification("booking_confirmation", { booking }, booking.email);
}

function notifyAppointmentConfirmation(appointment) {
  return buildNotification("appointment_confirmation", { appointment }, appointment.email);
}

function notifyVisaApplicationReceived(application) {
  return buildNotification("visa_application_received", { application }, application.email);
}

function notifyStudyApplicationReceived(application) {
  return buildNotification("study_application_received", { application }, application.email);
}

function notifyContactAcknowledgement(contact) {
  return buildNotification("contact_acknowledgement", { contact }, contact.email);
}

function notifyNewsletterWelcome(subscriber) {
  return buildNotification("newsletter_welcome", { subscriber }, subscriber.email);
}

function notifyAdminNewSubmission(submissionType, submission) {
  return buildNotification("admin_new_submission", { submissionType, submission }, "admin@suigeneris.com");
}

function sendEmailNotification(payload) {
  console.log("Notification payload ready:", payload);
  return Promise.resolve(payload);
}

function handleGlobalClick(event) {
  const target = event.target.closest("button");
  if (!target) return;
  const tableKey = target.dataset.table;
  const actionKey = target.dataset.action;
  if (tableKey) {
    loadModule(tableKey);
    return;
  }
  if (actionKey) {
    handleQuickAction(actionKey);
    return;
  }
  if (target.id === "logout-btn") {
    supabase.auth.signOut().then(() => {
      window.location.href = "../admin/login.html";
    });
    return;
  }
  if (target.id === "export-csv") {
    exportCurrentModuleCsv();
    return;
  }
  if (target.id === "print-view") {
    printCurrentView();
    return;
  }
  if (target.id === "module-action-button") {
    const config = getConfig(state.module);
    if (!config || config.isHome) {
      showToast("Select a module to create new content.", "info");
      return;
    }
    showToast(`Ready to create a new ${config.title.replace(/s$/, "")}.`, "success");
    return;
  }
  if (target.classList.contains("btn-view")) {
    const record = getRecordById(target.dataset.id);
    const config = getConfig(state.module);
    if (!record || !config) {
      showToast("Record unavailable.", "error");
      return;
    }
    openModal(record, config, "view");
    return;
  }
  if (target.classList.contains("btn-edit")) {
    const record = getRecordById(target.dataset.id);
    const config = getConfig(state.module);
    if (!record || !config) {
      showToast("Record unavailable.", "error");
      return;
    }
    openModal(record, config, "edit");
    return;
  }
  if (target.classList.contains("btn-delete")) {
    deleteRecord(target.dataset.id);
    return;
  }
  if (target.classList.contains("btn-print")) {
    const record = getRecordById(target.dataset.id);
    const config = getConfig(state.module);
    if (!record || !config) {
      showToast("Record unavailable.", "error");
      return;
    }
    printRecord(record, config);
    return;
  }
  if (["modal-close", "modal-cancel", "modal-save", "modal-print"].includes(target.id)) {
    handleModalAction(event);
    return;
  }
}

function handleRecordStatusChange(event) {
  const select = event.target.closest("select.record-status");
  if (!select) return;
  updateStatus(select.dataset.id, select.value);
}

function attachListeners() {
  elements.searchInput?.addEventListener("input", handleSearch);
  elements.statusFilterSelect?.addEventListener("change", handleFilter);
  elements.sortFieldSelect?.addEventListener("change", handleSort);
  elements.sortToggleBtn?.addEventListener("click", handleSortToggle);
  elements.previousPageBtn?.addEventListener("click", () => handlePageChange(-1));
  elements.nextPageBtn?.addEventListener("click", () => handlePageChange(1));
  elements.modalClose?.addEventListener("click", closeModal);
  elements.modalBackdrop?.addEventListener("click", event => { if (event.target === elements.modalBackdrop) closeModal(); });
  document.addEventListener("click", handleGlobalClick);
  document.addEventListener("change", handleRecordStatusChange);
}

function initialize() {
  attachListeners();
  loadDashboardStats();
  loadModule("home");
}

initialize();
'''

Path(r'c:\Users\BUYPC COMPUTERS\Desktop\Sui-Generis-Travels-and-Tours\admin\dashboard.html').write_text(html, encoding='utf-8')
Path(r'c:\Users\BUYPC COMPUTERS\Desktop\Sui-Generis-Travels-and-Tours\css\dashboard.css').write_text(css, encoding='utf-8')
Path(r'c:\Users\BUYPC COMPUTERS\Desktop\Sui-Generis-Travels-and-Tours\js\dashboard.js').write_text(js, encoding='utf-8')
print('done')
