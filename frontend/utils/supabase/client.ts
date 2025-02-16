import { createBrowserClient } from "@supabase/ssr";

const supabaseKey: string | undefined = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY;
const supabaseUrl: string | undefined = process.env.NEXT_PUBLIC_SUPABASE_BROWSER_URL;

export const createClient = () => {
  if (!supabaseKey || !supabaseUrl) {
    throw new Error("Supabase URL and Supabase Key must be provided.");
  }
  return createBrowserClient(supabaseUrl, supabaseKey);
};
