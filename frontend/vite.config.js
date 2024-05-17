import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { resolve } from 'path'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  build: {
    rollupOptions: {
      input: {
          index: resolve(__dirname, 'index.html'),
          studrada: resolve(__dirname, 'studrada.html'),
          about: resolve(__dirname, 'about.html'),
      }
    }
  }
})
