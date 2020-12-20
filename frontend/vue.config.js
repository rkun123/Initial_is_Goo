module.exports = {
  devServer: {
    proxy: {
      '/': {
        target: 'https://initial-is-goo.herokuapp.com/',
        wss: true,
        changeOrigin: true
      }
    }
  },
};
