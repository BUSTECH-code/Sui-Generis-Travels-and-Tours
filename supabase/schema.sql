-- =============================================================================
-- SUI-GENERIS TRAVELS AND TOURS LTD
-- PRODUCTION DATABASE SCHEMA
-- PART 1 - EXTENSIONS, FUNCTIONS, CORE TABLES
-- =============================================================================

-- ============================================================================
-- EXTENSIONS
-- ============================================================================

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS pgcrypto;

-- ============================================================================
-- UPDATE TIMESTAMP FUNCTION
-- ============================================================================

CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- ============================================================================
-- PROFILES
-- ============================================================================

CREATE TABLE IF NOT EXISTS public.profiles (

    id UUID PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE,

    full_name TEXT,

    email TEXT UNIQUE NOT NULL,

    phone TEXT,

    avatar_url TEXT,

    created_at TIMESTAMPTZ DEFAULT NOW(),

    updated_at TIMESTAMPTZ DEFAULT NOW()

);

-- ============================================================================
-- ADMINS
-- ============================================================================

CREATE TABLE IF NOT EXISTS public.admins (

    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

    profile_id UUID NOT NULL REFERENCES public.profiles(id) ON DELETE CASCADE,

    username TEXT UNIQUE NOT NULL,

    role TEXT NOT NULL DEFAULT 'admin'
        CHECK (role IN ('admin','manager','super_admin')),

    active BOOLEAN DEFAULT TRUE,

    created_at TIMESTAMPTZ DEFAULT NOW(),

    updated_at TIMESTAMPTZ DEFAULT NOW()

);

-- ============================================================================
-- WEBSITE SETTINGS
-- ============================================================================

CREATE TABLE IF NOT EXISTS public.settings (

    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

    company_name TEXT,

    email TEXT,

    phone_1 TEXT,

    phone_2 TEXT,

    phone_3 TEXT,

    office_address TEXT,

    facebook TEXT,

    instagram TEXT,

    twitter TEXT,

    whatsapp TEXT,

    youtube TEXT,

    bank_name_1 TEXT,

    account_name_1 TEXT,

    account_number_1 TEXT,

    bank_name_2 TEXT,

    account_name_2 TEXT,

    account_number_2 TEXT,

    created_at TIMESTAMPTZ DEFAULT NOW(),

    updated_at TIMESTAMPTZ DEFAULT NOW()

);

-- ============================================================================
-- UPDATE TRIGGERS
-- ============================================================================

CREATE TRIGGER trg_profiles_updated
BEFORE UPDATE
ON public.profiles
FOR EACH ROW
EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER trg_admins_updated
BEFORE UPDATE
ON public.admins
FOR EACH ROW
EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER trg_settings_updated
BEFORE UPDATE
ON public.settings
FOR EACH ROW
EXECUTE FUNCTION update_updated_at_column();

-- ============================================================================
-- INDEXES
-- ============================================================================

CREATE INDEX IF NOT EXISTS idx_profiles_email
ON public.profiles(email);

CREATE INDEX IF NOT EXISTS idx_admins_username
ON public.admins(username);

CREATE INDEX IF NOT EXISTS idx_admins_role
ON public.admins(role);

-- =============================================================================
-- PART 2 - CUSTOMER SERVICE TABLES
-- =============================================================================

-- ============================================================================
-- BOOKINGS
-- ============================================================================

CREATE TABLE IF NOT EXISTS public.bookings (

    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

    booking_reference TEXT UNIQUE DEFAULT (
        'SGT-' ||
        TO_CHAR(NOW(),'YYYYMMDD') ||
        '-' ||
        UPPER(SUBSTRING(gen_random_uuid()::TEXT,1,6))
    ),

    fullname TEXT NOT NULL,

    email TEXT NOT NULL,

    phone TEXT NOT NULL,

    trip_type TEXT DEFAULT 'one_way'
        CHECK (trip_type IN ('one_way','round_trip','multi_city')),

    departure_city TEXT NOT NULL,

    destination_city TEXT NOT NULL,

    departure_date DATE NOT NULL,

    return_date DATE,

    adults INT DEFAULT 1 CHECK(adults>=1),

    children INT DEFAULT 0 CHECK(children>=0),

    infants INT DEFAULT 0 CHECK(infants>=0),

    cabin_class TEXT DEFAULT 'Economy'
        CHECK (cabin_class IN (
            'Economy',
            'Premium Economy',
            'Business',
            'First'
        )),

    airline_preference TEXT,

    special_requests TEXT,

    payment_status TEXT DEFAULT 'pending'
        CHECK(payment_status IN(
            'pending',
            'paid',
            'refunded'
        )),

    booking_status TEXT DEFAULT 'pending'
        CHECK(booking_status IN(
            'pending',
            'reviewing',
            'quoted',
            'ticketed',
            'completed',
            'cancelled'
        )),

    admin_notes TEXT,

    created_at TIMESTAMPTZ DEFAULT NOW(),

    updated_at TIMESTAMPTZ DEFAULT NOW()

);

CREATE TRIGGER trg_bookings_updated
BEFORE UPDATE
ON public.bookings
FOR EACH ROW
EXECUTE FUNCTION update_updated_at_column();

CREATE INDEX idx_bookings_email
ON public.bookings(email);

CREATE INDEX idx_bookings_status
ON public.bookings(booking_status);

CREATE INDEX idx_bookings_created
ON public.bookings(created_at DESC);

-- ============================================================================
-- VISA APPLICATIONS
-- ============================================================================

CREATE TABLE IF NOT EXISTS public.visa_applications (

    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

    fullname TEXT NOT NULL,

    email TEXT NOT NULL,

    phone TEXT NOT NULL,

    nationality TEXT,

    destination_country TEXT NOT NULL,

    visa_category TEXT NOT NULL,

    passport_number TEXT,

    passport_expiry DATE,

    travel_date DATE,

    notes TEXT,

    passport_url TEXT,

    status TEXT DEFAULT 'pending'
        CHECK(status IN(
            'pending',
            'documents_required',
            'processing',
            'approved',
            'rejected',
            'completed'
        )),

    admin_notes TEXT,

    created_at TIMESTAMPTZ DEFAULT NOW(),

    updated_at TIMESTAMPTZ DEFAULT NOW()

);

CREATE TRIGGER trg_visa_updated
BEFORE UPDATE
ON public.visa_applications
FOR EACH ROW
EXECUTE FUNCTION update_updated_at_column();

CREATE INDEX idx_visa_status
ON public.visa_applications(status);

CREATE INDEX idx_visa_email
ON public.visa_applications(email);

-- ============================================================================
-- STUDY ABROAD APPLICATIONS
-- ============================================================================

CREATE TABLE IF NOT EXISTS public.study_applications (

    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

    fullname TEXT NOT NULL,

    email TEXT NOT NULL,

    phone TEXT NOT NULL,

    country TEXT NOT NULL,

    institution TEXT,

    course TEXT,

    qualification TEXT,

    preferred_intake TEXT,

    scholarship_interest BOOLEAN DEFAULT FALSE,

    english_test TEXT,

    work_experience TEXT,

    message TEXT,

    passport_url TEXT,

    cv_url TEXT,

    transcript_url TEXT,

    status TEXT DEFAULT 'pending'
        CHECK(status IN(
            'pending',
            'under_review',
            'offer_received',
            'visa_stage',
            'completed',
            'rejected'
        )),

    admin_notes TEXT,

    created_at TIMESTAMPTZ DEFAULT NOW(),

    updated_at TIMESTAMPTZ DEFAULT NOW()

);

CREATE TRIGGER trg_study_updated
BEFORE UPDATE
ON public.study_applications
FOR EACH ROW
EXECUTE FUNCTION update_updated_at_column();

CREATE INDEX idx_study_email
ON public.study_applications(email);

CREATE INDEX idx_study_status
ON public.study_applications(status);

-- ============================================================================
-- APPOINTMENTS
-- ============================================================================

CREATE TABLE IF NOT EXISTS public.appointments (

    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

    fullname TEXT NOT NULL,

    email TEXT NOT NULL,

    phone TEXT NOT NULL,

    service TEXT NOT NULL,

    appointment_date TIMESTAMPTZ NOT NULL,

    notes TEXT,

    status TEXT DEFAULT 'pending'
        CHECK(status IN(
            'pending',
            'scheduled',
            'completed',
            'cancelled'
        )),

    created_at TIMESTAMPTZ DEFAULT NOW(),

    updated_at TIMESTAMPTZ DEFAULT NOW()

);

CREATE TRIGGER trg_appointments_updated
BEFORE UPDATE
ON public.appointments
FOR EACH ROW
EXECUTE FUNCTION update_updated_at_column();

-- ============================================================================
-- CONTACT MESSAGES
-- ============================================================================

CREATE TABLE IF NOT EXISTS public.contacts (

    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

    fullname TEXT NOT NULL,

    email TEXT NOT NULL,

    phone TEXT,

    subject TEXT,

    message TEXT NOT NULL,

    status TEXT DEFAULT 'new'
        CHECK(status IN(
            'new',
            'read',
            'replied',
            'closed'
        )),

    created_at TIMESTAMPTZ DEFAULT NOW(),

    updated_at TIMESTAMPTZ DEFAULT NOW()

);

CREATE TRIGGER trg_contacts_updated
BEFORE UPDATE
ON public.contacts
FOR EACH ROW
EXECUTE FUNCTION update_updated_at_column();

-- ============================================================================
-- NEWSLETTER
-- ============================================================================

CREATE TABLE IF NOT EXISTS public.newsletter (

    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

    email TEXT UNIQUE NOT NULL,

    active BOOLEAN DEFAULT TRUE,

    created_at TIMESTAMPTZ DEFAULT NOW()

);

CREATE INDEX idx_newsletter_email
ON public.newsletter(email);

-- =============================================================================
-- PART 3 - CONTENT MANAGEMENT SYSTEM (CMS)
-- =============================================================================

-- ============================================================================
-- BLOG POSTS
-- ============================================================================

CREATE TABLE IF NOT EXISTS public.blogs (

    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

    title TEXT NOT NULL,

    slug TEXT UNIQUE NOT NULL,

    excerpt TEXT,

    content TEXT NOT NULL,

    cover_image TEXT,

    author TEXT DEFAULT 'SUI-GENERIS TRAVELS',

    category TEXT DEFAULT 'Travel',

    featured BOOLEAN DEFAULT FALSE,

    published BOOLEAN DEFAULT FALSE,

    views INT DEFAULT 0,

    seo_title TEXT,

    seo_description TEXT,

    is_deleted BOOLEAN DEFAULT FALSE,

    created_at TIMESTAMPTZ DEFAULT NOW(),

    updated_at TIMESTAMPTZ DEFAULT NOW()

);

CREATE TRIGGER trg_blogs_updated
BEFORE UPDATE
ON public.blogs
FOR EACH ROW
EXECUTE FUNCTION update_updated_at_column();

CREATE INDEX idx_blog_slug
ON public.blogs(slug);

CREATE INDEX idx_blog_published
ON public.blogs(published);

CREATE INDEX idx_blog_featured
ON public.blogs(featured);

-- ============================================================================
-- GALLERY
-- ============================================================================

CREATE TABLE IF NOT EXISTS public.gallery (

    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

    title TEXT NOT NULL,

    category TEXT DEFAULT 'Travel',

    image_url TEXT NOT NULL,

    description TEXT,

    featured BOOLEAN DEFAULT FALSE,

    display_order INT DEFAULT 0,

    is_deleted BOOLEAN DEFAULT FALSE,

    created_at TIMESTAMPTZ DEFAULT NOW(),

    updated_at TIMESTAMPTZ DEFAULT NOW()

);

CREATE TRIGGER trg_gallery_updated
BEFORE UPDATE
ON public.gallery
FOR EACH ROW
EXECUTE FUNCTION update_updated_at_column();

CREATE INDEX idx_gallery_category
ON public.gallery(category);

CREATE INDEX idx_gallery_featured
ON public.gallery(featured);

-- ============================================================================
-- TESTIMONIALS
-- ============================================================================

CREATE TABLE IF NOT EXISTS public.testimonials (

    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

    name TEXT NOT NULL,

    country TEXT,

    rating INT DEFAULT 5
        CHECK(rating BETWEEN 1 AND 5),

    message TEXT NOT NULL,

    image_url TEXT,

    featured BOOLEAN DEFAULT FALSE,

    approved BOOLEAN DEFAULT FALSE,

    created_at TIMESTAMPTZ DEFAULT NOW(),

    updated_at TIMESTAMPTZ DEFAULT NOW()

);

CREATE TRIGGER trg_testimonials_updated
BEFORE UPDATE
ON public.testimonials
FOR EACH ROW
EXECUTE FUNCTION update_updated_at_column();

CREATE INDEX idx_testimonials_approved
ON public.testimonials(approved);

-- ============================================================================
-- SPECIAL OFFERS
-- ============================================================================

CREATE TABLE IF NOT EXISTS public.special_offers (

    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

    title TEXT NOT NULL,

    description TEXT,

    image_url TEXT,

    discount_label TEXT,

    start_date DATE,

    end_date DATE,

    active BOOLEAN DEFAULT TRUE,

    created_at TIMESTAMPTZ DEFAULT NOW(),

    updated_at TIMESTAMPTZ DEFAULT NOW()

);

CREATE TRIGGER trg_special_offers_updated
BEFORE UPDATE
ON public.special_offers
FOR EACH ROW
EXECUTE FUNCTION update_updated_at_column();

CREATE INDEX idx_offers_active
ON public.special_offers(active);

-- ============================================================================
-- ACTIVITY LOGS
-- ============================================================================

CREATE TABLE IF NOT EXISTS public.activity_logs (

    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

    admin_id UUID REFERENCES public.admins(id) ON DELETE SET NULL,

    action TEXT NOT NULL,

    table_name TEXT,

    record_id UUID,

    description TEXT,

    created_at TIMESTAMPTZ DEFAULT NOW()

);

CREATE INDEX idx_activity_created
ON public.activity_logs(created_at DESC);

CREATE INDEX idx_activity_admin
ON public.activity_logs(admin_id);

-- =============================================================================
-- PART 4 - STORAGE BUCKETS & RLS
-- =============================================================================

-- ============================================================================
-- STORAGE BUCKETS
-- ============================================================================

INSERT INTO storage.buckets (id, name, public)
VALUES
('gallery', 'gallery', true),
('blog-images', 'blog-images', true),
('hero-images', 'hero-images', true),
('logos', 'logos', true),
('testimonials', 'testimonials', true),
('documents', 'documents', false)
ON CONFLICT (id) DO NOTHING;

-- ============================================================================
-- ENABLE RLS
-- ============================================================================

ALTER TABLE public.profiles ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.admins ENABLE ROW LEVEL SECURITY;

ALTER TABLE public.bookings ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.visa_applications ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.study_applications ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.appointments ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.contacts ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.newsletter ENABLE ROW LEVEL SECURITY;

ALTER TABLE public.blogs ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.gallery ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.testimonials ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.special_offers ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.settings ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.activity_logs ENABLE ROW LEVEL SECURITY;

-- ============================================================================
-- PUBLIC INSERT POLICIES
-- ============================================================================

CREATE POLICY "Public booking insert"
ON public.bookings
FOR INSERT
TO anon
WITH CHECK (true);

CREATE POLICY "Public visa insert"
ON public.visa_applications
FOR INSERT
TO anon
WITH CHECK (true);

CREATE POLICY "Public study insert"
ON public.study_applications
FOR INSERT
TO anon
WITH CHECK (true);

CREATE POLICY "Public appointment insert"
ON public.appointments
FOR INSERT
TO anon
WITH CHECK (true);

CREATE POLICY "Public contact insert"
ON public.contacts
FOR INSERT
TO anon
WITH CHECK (true);

CREATE POLICY "Public newsletter insert"
ON public.newsletter
FOR INSERT
TO anon
WITH CHECK (true);

CREATE POLICY "Public testimonial insert"
ON public.testimonials
FOR INSERT
TO anon
WITH CHECK (true);

-- ============================================================================
-- PUBLIC READ
-- ============================================================================

CREATE POLICY "Read published blogs"
ON public.blogs
FOR SELECT
TO anon
USING (
    published = true
    AND is_deleted = false
);

CREATE POLICY "Read gallery"
ON public.gallery
FOR SELECT
TO anon
USING (
    is_deleted = false
);

CREATE POLICY "Read approved testimonials"
ON public.testimonials
FOR SELECT
TO anon
USING (
    approved = true
);

CREATE POLICY "Read active offers"
ON public.special_offers
FOR SELECT
TO anon
USING (
    active = true
);

CREATE POLICY "Read settings"
ON public.settings
FOR SELECT
TO anon
USING (true);

-- ============================================================================
-- AUTHENTICATED ACCESS
-- ============================================================================

CREATE POLICY "Authenticated full bookings"
ON public.bookings
FOR ALL
TO authenticated
USING (true)
WITH CHECK (true);

CREATE POLICY "Authenticated full visa"
ON public.visa_applications
FOR ALL
TO authenticated
USING (true)
WITH CHECK (true);

CREATE POLICY "Authenticated full study"
ON public.study_applications
FOR ALL
TO authenticated
USING (true)
WITH CHECK (true);

CREATE POLICY "Authenticated full appointments"
ON public.appointments
FOR ALL
TO authenticated
USING (true)
WITH CHECK (true);

CREATE POLICY "Authenticated full contacts"
ON public.contacts
FOR ALL
TO authenticated
USING (true)
WITH CHECK (true);

CREATE POLICY "Authenticated full newsletter"
ON public.newsletter
FOR ALL
TO authenticated
USING (true)
WITH CHECK (true);

CREATE POLICY "Authenticated full blogs"
ON public.blogs
FOR ALL
TO authenticated
USING (true)
WITH CHECK (true);

CREATE POLICY "Authenticated full gallery"
ON public.gallery
FOR ALL
TO authenticated
USING (true)
WITH CHECK (true);

CREATE POLICY "Authenticated full testimonials"
ON public.testimonials
FOR ALL
TO authenticated
USING (true)
WITH CHECK (true);

CREATE POLICY "Authenticated full offers"
ON public.special_offers
FOR ALL
TO authenticated
USING (true)
WITH CHECK (true);

CREATE POLICY "Authenticated full settings"
ON public.settings
FOR ALL
TO authenticated
USING (true)
WITH CHECK (true);

CREATE POLICY "Authenticated full admins"
ON public.admins
FOR ALL
TO authenticated
USING (true)
WITH CHECK (true);

CREATE POLICY "Authenticated full profiles"
ON public.profiles
FOR ALL
TO authenticated
USING (true)
WITH CHECK (true);

CREATE POLICY "Authenticated full activity"
ON public.activity_logs
FOR ALL
TO authenticated
USING (true)
WITH CHECK (true);

-- =============================================================================
-- PART 5 - ADMIN SECURITY
-- =============================================================================

-- ============================================================================
-- HELPER FUNCTION
-- Returns TRUE only if logged-in user is an active admin
-- ============================================================================

CREATE OR REPLACE FUNCTION public.is_admin()
RETURNS BOOLEAN
LANGUAGE sql
STABLE
SECURITY DEFINER
AS $$
SELECT EXISTS (
    SELECT 1
    FROM public.admins a
    WHERE a.profile_id = auth.uid()
      AND a.active = TRUE
);
$$;

-- ============================================================================
-- DROP OLD AUTHENTICATED POLICIES
-- ============================================================================

DROP POLICY IF EXISTS "Authenticated full bookings" ON public.bookings;
DROP POLICY IF EXISTS "Authenticated full visa" ON public.visa_applications;
DROP POLICY IF EXISTS "Authenticated full study" ON public.study_applications;
DROP POLICY IF EXISTS "Authenticated full appointments" ON public.appointments;
DROP POLICY IF EXISTS "Authenticated full contacts" ON public.contacts;
DROP POLICY IF EXISTS "Authenticated full newsletter" ON public.newsletter;
DROP POLICY IF EXISTS "Authenticated full blogs" ON public.blogs;
DROP POLICY IF EXISTS "Authenticated full gallery" ON public.gallery;
DROP POLICY IF EXISTS "Authenticated full testimonials" ON public.testimonials;
DROP POLICY IF EXISTS "Authenticated full offers" ON public.special_offers;
DROP POLICY IF EXISTS "Authenticated full settings" ON public.settings;
DROP POLICY IF EXISTS "Authenticated full admins" ON public.admins;
DROP POLICY IF EXISTS "Authenticated full profiles" ON public.profiles;
DROP POLICY IF EXISTS "Authenticated full activity" ON public.activity_logs;

-- ============================================================================
-- ADMIN ONLY POLICIES
-- ============================================================================

CREATE POLICY "Admins manage bookings"
ON public.bookings
FOR ALL
TO authenticated
USING (public.is_admin())
WITH CHECK (public.is_admin());

CREATE POLICY "Admins manage visa"
ON public.visa_applications
FOR ALL
TO authenticated
USING (public.is_admin())
WITH CHECK (public.is_admin());

CREATE POLICY "Admins manage study"
ON public.study_applications
FOR ALL
TO authenticated
USING (public.is_admin())
WITH CHECK (public.is_admin());

CREATE POLICY "Admins manage appointments"
ON public.appointments
FOR ALL
TO authenticated
USING (public.is_admin())
WITH CHECK (public.is_admin());

CREATE POLICY "Admins manage contacts"
ON public.contacts
FOR ALL
TO authenticated
USING (public.is_admin())
WITH CHECK (public.is_admin());

CREATE POLICY "Admins manage newsletter"
ON public.newsletter
FOR ALL
TO authenticated
USING (public.is_admin())
WITH CHECK (public.is_admin());

CREATE POLICY "Admins manage blogs"
ON public.blogs
FOR ALL
TO authenticated
USING (public.is_admin())
WITH CHECK (public.is_admin());

CREATE POLICY "Admins manage gallery"
ON public.gallery
FOR ALL
TO authenticated
USING (public.is_admin())
WITH CHECK (public.is_admin());

CREATE POLICY "Admins manage testimonials"
ON public.testimonials
FOR ALL
TO authenticated
USING (public.is_admin())
WITH CHECK (public.is_admin());

CREATE POLICY "Admins manage offers"
ON public.special_offers
FOR ALL
TO authenticated
USING (public.is_admin())
WITH CHECK (public.is_admin());

CREATE POLICY "Admins manage settings"
ON public.settings
FOR ALL
TO authenticated
USING (public.is_admin())
WITH CHECK (public.is_admin());

CREATE POLICY "Admins manage admins"
ON public.admins
FOR ALL
TO authenticated
USING (public.is_admin())
WITH CHECK (public.is_admin());

CREATE POLICY "Admins manage profiles"
ON public.profiles
FOR ALL
TO authenticated
USING (public.is_admin())
WITH CHECK (public.is_admin());

CREATE POLICY "Admins manage activity"
ON public.activity_logs
FOR ALL
TO authenticated
USING (public.is_admin())
WITH CHECK (public.is_admin());

-- =============================================================================
-- PART 6 - DEFAULT SETTINGS & PERFORMANCE
-- =============================================================================

-- Default company settings
INSERT INTO public.settings (
    company_name,
    email,
    phone_1,
    phone_2,
    phone_3,
    office_address,
    bank_name_1,
    account_name_1,
    account_number_1,
    bank_name_2,
    account_name_2,
    account_number_2
)
SELECT
'SUIGENERIS TRAVELS AND TOURS LTD',
'info@suigeneristravel.com',
'08171421897',
'07060907368',
'08053521324',
'Suite D19, Melita Plaza, Area 11 Garki, FCT Abuja',
'PROVIDUS BANK',
'SUIGENERIS TRAVELS AND TOURS LTD',
'1307828780',
'ZENITH BANK',
'SUIGENERIS TRAVELS AND TOURS LTD',
'1015677308'
WHERE NOT EXISTS (
    SELECT 1 FROM public.settings
);

-- ===========================================================
-- EXTRA INDEXES
-- ===========================================================

CREATE INDEX IF NOT EXISTS idx_bookings_reference
ON public.bookings(booking_reference);

CREATE INDEX IF NOT EXISTS idx_bookings_departure
ON public.bookings(departure_city);

CREATE INDEX IF NOT EXISTS idx_bookings_destination
ON public.bookings(destination_city);

CREATE INDEX IF NOT EXISTS idx_visa_country
ON public.visa_applications(destination_country);

CREATE INDEX IF NOT EXISTS idx_study_country
ON public.study_applications(country);

CREATE INDEX IF NOT EXISTS idx_contacts_created
ON public.contacts(created_at DESC);

CREATE INDEX IF NOT EXISTS idx_gallery_order
ON public.gallery(display_order);

CREATE INDEX IF NOT EXISTS idx_special_offer_dates
ON public.special_offers(start_date,end_date);

-- ===========================================================
-- COMMENTS
-- ===========================================================

COMMENT ON TABLE public.bookings IS 'Flight, Tour and Holiday bookings';

COMMENT ON TABLE public.study_applications IS 'Study abroad applications';

COMMENT ON TABLE public.visa_applications IS 'Visa applications';

COMMENT ON TABLE public.blogs IS 'Website blog posts';

COMMENT ON TABLE public.gallery IS 'Gallery images';

COMMENT ON TABLE public.settings IS 'Website settings';

COMMENT ON TABLE public.activity_logs IS 'Administrative audit logs';