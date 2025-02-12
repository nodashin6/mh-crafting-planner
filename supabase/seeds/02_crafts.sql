DO $$
DECLARE
    craft_data jsonb := '[
        {
            "products": ["回復薬"],
            "precursors": ["薬草", "アオキノコ"],
            "required_hours": 2,
            "yield": 0.90
        }, 
        {
            "products": ["栄養剤"],
            "precursors": ["不死虫", "アオキノコ"],
            "required_hours": 2,
            "yield": 0.90
        },
        {
            "products": ["増強剤"],
            "precursors": ["にが虫", "ハチミツ"],
            "required_hours": 2,
            "yield": 0.75
        },
        {
            "products": ["解毒薬"],
            "precursors": ["げどく草", "アオキノコ"],
            "required_hours": 2,
            "yield": 0.95
        },
        {
            "products": ["活力剤"],
            "precursors": ["増強剤", "マンドラゴラ"],
            "required_hours": 2,
            "yield": 0.75
        },
        {
            "products": ["回復薬G"],
            "precursors": ["回復薬", "ハチミツ"],
            "required_hours": 2,
            "yield": 0.95
        },
        {
            "products": ["栄養剤G"],
            "precursors": ["不死虫", "ハチミツ"],
            "required_hours": 2,
            "yield": 0.75
        },
        {
            "products": ["秘薬"],
            "precursors": ["栄養剤G", "マンドラゴラ"],
            "required_hours": 2,
            "yield": 0.65
        },
        {
            "products": ["古の秘薬"],
            "precursors": ["活力剤", "ケルビの角"],
            "required_hours": 2,
            "yield": 0.55
        }
    ]'::jsonb;
    craft jsonb;
    product text;
    precursor text;
    craft_id uuid;
    craft_array jsonb[];
BEGIN
    -- Convert JSON array to PostgreSQL array
    craft_array := ARRAY(SELECT jsonb_array_elements(craft_data));

    -- Loop through each craft entry
    FOREACH craft IN ARRAY craft_array LOOP
        -- Generate a new UUID for the craft
        craft_id := uuid_generate_v4();

        -- Insert into crafts table
        INSERT INTO public.crafts (id, required_hours, yield)
        VALUES (craft_id, (craft->>'required_hours')::numeric, (craft->>'yield')::numeric);

        -- Insert into precursors table
        FOR precursor IN SELECT * FROM jsonb_array_elements_text(craft->'precursors') LOOP
            INSERT INTO public.precursors (id, item_id, craft_id)
            VALUES (uuid_generate_v4(), (SELECT id FROM public.items WHERE name = precursor LIMIT 1), craft_id);
        END LOOP;

        -- Insert into products table
        FOR product IN SELECT * FROM jsonb_array_elements_text(craft->'products') LOOP
            INSERT INTO public.products (id, item_id, craft_id)
            VALUES (uuid_generate_v4(), (SELECT id FROM public.items WHERE name = product LIMIT 1), craft_id);
        END LOOP;
    END LOOP;
END $$;