import { createClient } from "https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2/+esm";

const SUPABASE_URL = "https://brudufqolikgmecykdnj.supabase.co";

const SUPABASE_ANON_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJydWR1ZnFvbGlrZ21lY3lrZG5qIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODQ3NjAxMzcsImV4cCI6MjEwMDMzNjEzN30.8ZvnWRRcScCnm5CuVDnkHc0u_i_CW_w5U4hQWm5hPXw";

export const supabase = createClient(
    SUPABASE_URL,
    SUPABASE_ANON_KEY,
    {
        auth: {
            persistSession: true,
            autoRefreshToken: true,
            detectSessionInUrl: true
        }
    }
);