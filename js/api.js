import { supabase } from '../supabase/client.js';

export const API = {
  // ==========================================
  // PUBLIC FORM SUBMISSIONS (Lead Generation)
  // ==========================================

  /**
   * Generic form handler: saves record to Supabase DB
   * @param {string} table - Target table name
   * @param {Object} payload - Form field values
   */
  async submitForm(table, payload) {
    // 1. Store in Supabase DB
    const { data, error } = await supabase
      .from(table)
      .insert([payload])
      .select();

    if (error) {
      console.error(`Supabase Insert Error [${table}]:`, error);
      throw new Error(error.message || 'Failed to submit form.');
    }

    // 2. Optional: Trigger Webhook or Email service if configured
    this.dispatchNotification(table, payload).catch(err => {
      // Non-blocking log so form submission succeeds even without notification backend
      console.warn('Notification dispatch skipped or failed:', err);
    });

    return data;
  },

  async dispatchNotification(formType, payload) {
    // Optional client-side notification trigger (e.g. EmailJS or Webhook)
    // If you use Supabase Database Webhooks in the dashboard, you don't even need this function!
    return true;
  },

  // ==========================================
  // PUBLIC CONTENT FETCHERS
  // ==========================================

  async getPublishedBlogs(limit = 10) {
    const { data, error } = await supabase
      .from('blogs')
      .select('*')
      .eq('published', true)
      .eq('is_deleted', false)
      .order('created_at', { ascending: false })
      .limit(limit);

    if (error) throw error;
    return data;
  },

  async getBlogBySlug(slug) {
    const { data, error } = await supabase
      .from('blogs')
      .select('*')
      .eq('slug', slug)
      .eq('published', true)
      .single();

    if (error) throw error;
    return data;
  },

  async getGalleryItems(category = null) {
    let query = supabase
      .from('gallery')
      .select('*')
      .eq('is_deleted', false)
      .order('created_at', { ascending: false });

    if (category) {
      query = query.eq('category', category);
    }

    const { data, error } = await query;
    if (error) throw error;
    return data;
  },

  async getApprovedTestimonials() {
    const { data, error } = await supabase
      .from('testimonials')
      .select('*')
      .eq('approved', true)
      .order('created_at', { ascending: false });

    if (error) throw error;
    return data;
  },

  // ==========================================
  // ADMIN DASHBOARD DATA AGGREGATION
  // ==========================================

  async getAdminStats() {
    const [
      { count: bookings },
      { count: visas },
      { count: study },
      { count: appointments }
    ] = await Promise.all([
      supabase.from('bookings').select('*', { count: 'exact', head: true }).eq('status', 'pending'),
      supabase.from('visa_applications').select('*', { count: 'exact', head: true }).eq('status', 'pending'),
      supabase.from('study_applications').select('*', { count: 'exact', head: true }).eq('status', 'pending'),
      supabase.from('appointments').select('*', { count: 'exact', head: true }).eq('status', 'pending')
    ]);

    return { bookings, visas, study, appointments };
  },

  async getAdminRecords(table, page = 1, limit = 20) {
    const from = (page - 1) * limit;
    const to = from + limit - 1;

    const { data, error, count } = await supabase
      .from(table)
      .select('*', { count: 'exact' })
      .order('created_at', { ascending: false })
      .range(from, to);

    if (error) throw error;
    return { data, count };
  },

  async updateRecordStatus(table, id, status) {
    const { data, error } = await supabase
      .from(table)
      .update({ status })
      .eq('id', id)
      .select();

    if (error) throw error;
    return data;
  },

  // ==========================================
  // STORAGE MANAGEMENT
  // ==========================================

  async uploadFile(bucket, filePath, file) {
    const { data, error } = await supabase.storage
      .from(bucket)
      .upload(filePath, file, {
        cacheControl: '3600',
        upsert: false
      });

    if (error) throw error;

    const { data: publicUrlData } = supabase.storage
      .from(bucket)
      .getPublicUrl(data.path);

    return publicUrlData.publicUrl;
  }
};