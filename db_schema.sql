CREATE TABLE IF NOT EXISTS "projects" (
	"id"	INTEGER NOT NULL,
	"title"	TEXT,
	"success_criteria"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE sqlite_sequence(name,seq);
CREATE TABLE IF NOT EXISTS "users" (
	"id"	INTEGER NOT NULL,
	"name"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "tasks" (
	"id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"title"	TEXT,
	"project_id"	INTEGER,
	"status"	TEXT,
	"description"	TEXT,
	"delegate_id"	INTEGER,
	"estimate"	INTEGER,
	"when"	TEXT,
	FOREIGN KEY("project_id") REFERENCES "projects"("id"),
	FOREIGN KEY("delegate_id") REFERENCES "users"("id")
);
