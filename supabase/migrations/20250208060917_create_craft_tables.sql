CREATE TABLE mixers (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    max_capacity INT NOT NULL,
    changeover_hours INT NOT NULL,
    default_facility BOOLEAN NOT NULL
);

CREATE TABLE crafts (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    required_hours INT NOT NULL,
    yield DOUBLE PRECISION NOT NULL
);

CREATE TABLE precursors (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    item_id UUID NOT NULL REFERENCES items(id) ON UPDATE CASCADE ON DELETE CASCADE,
    craft_id UUID NOT NULL REFERENCES crafts(id) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE products (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    item_id UUID NOT NULL REFERENCES items(id) ON UPDATE CASCADE ON DELETE CASCADE,
    craft_id UUID NOT NULL REFERENCES crafts(id) ON UPDATE CASCADE ON DELETE CASCADE
);
