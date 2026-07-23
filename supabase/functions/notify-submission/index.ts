// Native Deno.serve configuration for Supabase Edge Functions
const RESEND_API_KEY = Deno.env.get('RESEND_API_KEY');
const TWILIO_ACCOUNT_SID = Deno.env.get('TWILIO_ACCOUNT_SID');
const TWILIO_AUTH_TOKEN = Deno.env.get('TWILIO_AUTH_TOKEN');
const TWILIO_PHONE_NUMBER = Deno.env.get('TWILIO_PHONE_NUMBER');
const ADMIN_PHONE_NUMBER = Deno.env.get('ADMIN_PHONE_NUMBER');

const TARGET_EMAIL = 'info@suigeneristravel.com';

const corsHeaders = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Headers': 'authorization, x-client-info, apikey, content-type',
};

Deno.serve(async (req: Request): Promise<Response> => {
  if (req.method === 'OPTIONS') {
    return new Response('ok', { headers: corsHeaders });
  }

  try {
    const { formType, payload } = await req.json();

    const emailSubject = `[NEW LEAD] ${String(formType).toUpperCase().replace('_', ' ')} - ${payload.fullname || 'Client Inquiry'}`;
    
    const emailBody = `
      <div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; border: 1px solid #e2e8f0; border-radius: 8px; overflow: hidden;">
        <div style="background-color: #122466; color: #ffffff; padding: 20px; text-align: center;">
          <h2 style="margin: 0;">SUI-GENERIS TRAVELS & TOURS</h2>
          <p style="margin: 5px 0 0 0; font-size: 14px; opacity: 0.9;">New Submission Notification</p>
        </div>
        <div style="padding: 24px; color: #0f172a;">
          <h3 style="color: #108643; margin-top: 0;">Form Category: ${String(formType).toUpperCase()}</h3>
          <table style="width: 100%; border-collapse: collapse; margin-top: 15px;">
            ${Object.entries(payload).map(([key, val]) => `
              <tr style="border-bottom: 1px solid #f8fafc;">
                <td style="padding: 10px; font-weight: bold; text-transform: capitalize; color: #64748b; width: 35%;">${key.replace('_', ' ')}</td>
                <td style="padding: 10px; color: #0f172a;">${val || 'N/A'}</td>
              </tr>
            `).join('')}
          </table>
        </div>
      </div>
    `;

    // Dispatch Email
    if (RESEND_API_KEY) {
      await fetch('https://api.resend.com/emails', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${RESEND_API_KEY}`,
        },
        body: JSON.stringify({
          from: 'SUI-GENERIS System <notifications@suigeneristravel.com>',
          to: [TARGET_EMAIL],
          subject: emailSubject,
          html: emailBody,
        }),
      });
    }

    // Dispatch SMS via Twilio
    if (TWILIO_ACCOUNT_SID && TWILIO_AUTH_TOKEN && ADMIN_PHONE_NUMBER) {
      const smsMessage = `[SUI-GENERIS] New ${formType} from ${payload.fullname || 'Client'} (${payload.phone || 'No phone'}).`;
      const smsBody = new URLSearchParams({
        From: TWILIO_PHONE_NUMBER || '',
        To: ADMIN_PHONE_NUMBER,
        Body: smsMessage
      });

      await fetch(`https://api.twilio.com/2010-04-01/Accounts/${TWILIO_ACCOUNT_SID}/Messages.json`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
          'Authorization': `Basic ${btoa(`${TWILIO_ACCOUNT_SID}:${TWILIO_AUTH_TOKEN}`)}`
        },
        body: smsBody.toString()
      });
    }

    return new Response(JSON.stringify({ success: true }), {
      headers: { ...corsHeaders, 'Content-Type': 'application/json' },
      status: 200,
    });

  } catch (err: unknown) {
    const errorMessage = err instanceof Error ? err.message : 'Unknown error occurred';
    return new Response(JSON.stringify({ error: errorMessage }), {
      headers: { ...corsHeaders, 'Content-Type': 'application/json' },
      status: 500,
    });
  }
});