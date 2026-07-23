import { supabase } from '../supabase/client.js';

export const Auth = {
  /**
   * Authenticate admin via Supabase Auth
   * @param {string} email 
   * @param {string} password 
   */
  async login(email, password) {
    const { data, error } = await supabase.auth.signInWithPassword({
      email,
      password
    });
    if (error) throw error;
    return data;
  },

  /**
   * Terminate current admin session
   */
  async logout() {
    const { error } = await supabase.auth.signOut();
    if (error) throw error;
    window.location.href = '/login.html';
  },

  /**
   * Enforce admin protection on dashboard routes
   */
  async requireAuth() {
    const { data: { session } } = await supabase.auth.getSession();
    
    if (!session) {
      window.location.href = '/login.html';
      return null;
    }
    
    return session;
  },

  /**
   * Check session status without forced redirect
   */
  async getSession() {
    const { data: { session } } = await supabase.auth.getSession();
    return session;
  }
};