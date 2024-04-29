import { supabase } from "$lib/supabase";

export const load = async () => {
  const { data: links, error } = await supabase
    .from("links")
    .select("*")
    .order("date_created", { ascending: false });
  if (error) throw error;

  if (error) throw error;

  return {
    links,
  };
};
