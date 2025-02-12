CREATE OR REPLACE FUNCTION buy(savedata_id UUID, item_name TEXT, quantity INT) 
RETURNS VOID AS $$
DECLARE
    item RECORD;
BEGIN
    -- itemを買う
    SELECT * INTO item FROM public.items WHERE name = item_name LIMIT 1;

    INSERT INTO public.belongings (savedata_id, item_id, quantity)
    VALUES
        (savedata_id, item.id, quantity);

    UPDATE public.savedatas
    SET gold = gold - item.price * quantity
    WHERE id = savedata_id;
END;
$$ LANGUAGE plpgsql;