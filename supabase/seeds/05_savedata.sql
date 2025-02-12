DO $$ 
DECLARE
    this_uuid UUID := uuid_generate_v4();
BEGIN
    INSERT INTO public.savedatas (id, player_id, gold, current_day, current_hour)
    VALUES
        (this_uuid, (SELECT id FROM public.players WHERE name = 'Admin'), 1000, 0, 0);

    -- itemを買う
    PERFORM buy(this_uuid, '薬草', 10);
    PERFORM buy(this_uuid, 'アオキノコ', 10);
END $$;