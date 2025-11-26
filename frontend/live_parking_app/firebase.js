// firebase.js
import './firebase';
import { initializeApp } from 'firebase/app';

// Firebase 설정 정보
const firebaseConfig = {
  apiKey: 'AIzaSyCRjmaZ9pIbW6s-vOk1vIlh3ZBVYtgr0r8',
  authDomain: 'live-parking-eed8c.firebaseapp.com',
  projectId: 'live-parking-eed8c',
  storageBucket: 'live-parking-eed8c.firebasestorage.app',
  messagingSenderId: '763982831274',
  appId: '1:763982831274:web:fac32bba9c2a1e9677bad3',
  measurementId: 'G-71FSSH6CKD',
};

// Firebase 초기화
const app = initializeApp(firebaseConfig);

export default app;
