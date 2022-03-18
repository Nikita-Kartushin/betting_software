db = db.getSiblingDB("betting-software");
db.createCollection('user');
db.createUser({
  user: "agent",
  pwd: "1123581321",
  roles: [{ role: "readWrite", db: "betting-software" }],
});
