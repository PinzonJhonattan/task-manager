import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000/api',  // URL del backend
  headers: {
    'Content-Type': 'application/json',
  },
});

// Interceptor para añadir el token JWT a las solicitudes
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('access_token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export default api;