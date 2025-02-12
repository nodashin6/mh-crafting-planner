CREATE TABLE savedatas (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    player_id UUID NOT NULL REFERENCES players(id) ON UPDATE CASCADE ON DELETE CASCADE,
    gold INT NOT NULL,
    current_day INT NOT NULL,
    current_hour int NOT NULL
);

CREATE TABLE belongings (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    savedata_id UUID NOT NULL REFERENCES savedatas(id) ON UPDATE CASCADE ON DELETE CASCADE,
    item_id UUID NOT NULL REFERENCES items(id) ON UPDATE CASCADE ON DELETE CASCADE,
    quantity INT NOT NULL
);

CREATE TABLE facilities (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    savedata_id UUID NOT NULL REFERENCES savedatas(id) ON UPDATE CASCADE ON DELETE CASCADE,
    mixer_id UUID NOT NULL REFERENCES mixers(id) ON UPDATE CASCADE ON DELETE CASCADE
);


CREATE TABLE schedules (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    mixer_id UUID NOT NULL REFERENCES mixers(id) ON UPDATE CASCADE ON DELETE CASCADE,
    craft_id UUID NOT NULL REFERENCES crafts(id) ON UPDATE CASCADE ON DELETE CASCADE,
    quantity INT NOT NULL,
    start_day INT NOT NULL,
    start_hour INT NOT NULL,
    end_day INT NOT NULL,
    end_hour INT NOT NULL,
    has_completed BOOLEAN NOT NULL
);

CREATE TABLE orders (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    savedata_id UUID NOT NULL REFERENCES savedatas(id) ON UPDATE CASCADE ON DELETE CASCADE,
    product_id UUID NOT NULL REFERENCES products(id) ON UPDATE CASCADE ON DELETE CASCADE,
    quantity INT NOT NULL,
    due_day INT NOT NULL
);


CREATE TABLE messages (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    savedata_id UUID NOT NULL REFERENCES savedatas(id) ON UPDATE CASCADE ON DELETE CASCADE,
    message TEXT NOT NULL,
    day INT NOT NULL,
    hour INT NOT NULL
);

