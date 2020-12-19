module.exports = {
  devServer: {
    proxy: {
      '/': {
        target: 'https://b75aab941684.ngrok.io/',
        wss: true,
        changeOrigin: true
      }
    }
  },
};
