CREATE TABLE items (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name TEXT NOT NULL,
    leadtime INT NOT NULL,
    price INT NOT NULL,
    constraint items_name_unique unique (name)
);
