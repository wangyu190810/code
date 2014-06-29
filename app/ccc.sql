PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE posts (
	id INTEGER NOT NULL, 
	title VARCHAR NOT NULL, 
	text TEXT NOT NULL, 
	time VARCHAR NOT NULL, 
	PRIMARY KEY (id)
);
INSERT INTO "posts" VALUES(1,'qwereqr','23333','asdf');
INSERT INTO "posts" VALUES(2,'asdfasdfasdf','asdfasdfasdfasdf','asdf');
INSERT INTO "posts" VALUES(3,'','','asdf');
INSERT INTO "posts" VALUES(4,'asdfasfasdf','sd23423432','asdf');
INSERT INTO "posts" VALUES(5,'','','asdf');
CREATE TABLE comment (
	id INTEGER NOT NULL, 
	content INTEGER NOT NULL, 
	role_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(role_id) REFERENCES posts (id)
);
INSERT INTO "comment" VALUES(1,'qafasdfasdfasdf',4);
INSERT INTO "comment" VALUES(2,'qrfadsfasdfasdfasd',4);
INSERT INTO "comment" VALUES(3,'wefasfasdfasdfasdfasdf',4);
INSERT INTO "comment" VALUES(4,'asdfasdfjaosdfasdfnasdfoaosdfiaiodfoiaiodfoaidiaiodoaiodoasdo',4);
COMMIT;
