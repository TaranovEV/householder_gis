// import axios from "axios";
//
//
// const api = axios.create(
//   {baseUrl: 'http://127.0.0.1:8000/api'}
// )
//
//
// api.interceptors.response.use(
//   (response) => response,
//   async (error) => {
//     const originalRequest = error.config;
//
//     if (error.response.status === 401 && !originalRequest._retry) {
//       originalRequest._retry = true;
//       try {
//         const refreshToken = localStorage.getItem('refresh');
//         const response = await axios.post('http://127.0.0.1:8000/api/token/refresh/', {refreshToken});
//         const {token} = response.data.refresh
//         localStorage.setItem('accessToken', token)
//         originalRequest.headers.Authorization = `Bearer ${token}`;
//
//         return axios(originalRequest)
//       } catch (error) {
//         console.log(error)
//       }
//     }
//     return Promise.reject(error)
//   }
// )
// export default api;
