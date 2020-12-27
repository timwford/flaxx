##### upgrade #####
CREATE TABLE IF NOT EXISTS "moodmodel" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "mood" VARCHAR(255) NOT NULL,
    "ts" INT NOT NULL
);
COMMENT ON COLUMN "moodmodel"."mood" IS 'Mood being recorded: [''negative'', ''neutral'', ''positive'']';
COMMENT ON COLUMN "moodmodel"."ts" IS 'Epoch time';
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(20) NOT NULL,
    "content" TEXT NOT NULL
);
