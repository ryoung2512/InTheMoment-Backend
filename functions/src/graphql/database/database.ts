const db = require("firebase-admin");

// To generate a private key file for your service account:
// 1. In the Firebase console, open Settings > Service Accounts.
// 2. Click Generate New Private Key, then confirm by clicking Generate Key.
// 3. Store the JSON file in the `functions/resources/` directory

var serviceAccount = require("../../../resources/inthemoment-key.json");

db.initializeApp({
  credential: db.credential.cert(serviceAccount),
  databaseURL: "https://inthemoment-4e008-default-rtdb.firebaseio.com"
});

export default db;