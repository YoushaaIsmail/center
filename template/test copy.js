
import { initializeApp } from "firebase/app";
import { getMessaging,getToken } from "firebase/messaging";

const firebaseConfig = {
  apiKey: "AIzaSyCZlU0RyfTU1Qwx4ZpAaqCBbv03UzXZO-c",
  authDomain: "mycliproject-85e32.firebaseapp.com",
  databaseURL: "https://mycliproject-85e32-default-rtdb.firebaseio.com",
  projectId: "mycliproject-85e32",
  storageBucket: "mycliproject-85e32.appspot.com",
  messagingSenderId: "559508642472",
  appId: "1:559508642472:web:0bdf65ae194ba4daa0809d"
};

function requestPermission() {
  console.log('Requesting permission...');
  Notification.requestPermission().then((permission) => {
    if (permission === 'granted') {
      console.log('Notification permission granted.');
      const app = initializeApp(firebaseConfig); 
      const messaging = getMessaging(app);
      getToken(messaging, {vapidKey:'BNjmt8iZweqyX1kEMYhnGuVDLtyvz9HGD2242Lgm_T695TpUfd3AuOIpjgu1Ia9UJAPCm2eDvhKeUiroMpQLfX8'})
      .then((currentToken) => {
        if (currentToken) {
          console.log('currentToken', currentToken)
        } else {
          console.log('No registration token available. Request permission to generate one.');
        }
      }).catch((err) => {
        console.log('An error occurred while retrieving token. ', err);
      });
    } else {
      console.log('eror');
    }
  });
}

requestPermission();