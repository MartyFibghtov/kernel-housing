const { defineConfig } = require("@vue/cli-service");
module.exports = defineConfig({
  transpileDependencies: true,
  lintOnSave: false,
  allowedHosts: [
    '0.0.0.0'
  ]
});
