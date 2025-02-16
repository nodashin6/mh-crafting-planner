CREATE OR REPLACE FUNCTION create_player(plyer_id UUID, player_name TEXT) 
RETURNS VOID AS $$
BEGIN
    INSERT INTO players (id, name) VALUES (plyer_id, player_name);
END;
$$ LANGUAGE plpgsql;