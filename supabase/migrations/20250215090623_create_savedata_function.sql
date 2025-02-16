CREATE OR REPLACE FUNCTION create_savedata(player_id UUID, savedata_name TEXT) 
RETURNS VOID AS $$
DECLARE
    savedata_id UUID = uuid_generate_v4();
BEGIN
    INSERT INTO 
        savedatas (id, player_id, name, gold, current_day, current_hour) 
    VALUES 
        (savedata_id, player_id, savedata_name, 1000, 1, 9);

    -- Insert multiple records if there are multiple default facilities
    INSERT INTO
        facilities (savedata_id, mixer_id)
    SELECT
        savedata_id, id
    FROM
        mixers
    WHERE
        default_facility = TRUE;
END;
$$ LANGUAGE plpgsql;
