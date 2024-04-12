class TokenService {
  getLocalRefreshToken() {
    const user = JSON.parse(localStorage.getItem('refreshToken'))
    return user?.refreshToken
  }
  getLocalAccessToken() {
    const user = JSON.parse(localStorage.getItem('accessToken'))
    return user?.accessToken
  }
}
