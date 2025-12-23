
import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

// Optionally, set a default for REACT_APP_CODESPACE_NAME if not set
if (!process.env.REACT_APP_CODESPACE_NAME) {
  console.warn('REACT_APP_CODESPACE_NAME is not set. API calls may fail.');
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

reportWebVitals();
