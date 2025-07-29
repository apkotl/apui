<script setup>
defineProps({
  msg: {
    type: String,
    required: true,
  },
})


////////// - TEST START
import { ref, onMounted } from 'vue';

// 1. Объявление реактивных переменных
const apiData = ref(null); // Для хранения полученных JSON данных
const loading = ref(true); // Индикатор загрузки
const error = ref(null); // Для хранения ошибок

// API URL
const apiUrl = 'http://api.localhost/version?q=test+query+string'; 

// 2. Test --- Функция для загрузки данных
const fetchData = async () => {
  loading.value = true;
  error.value = null; // Сбрасываем ошибку перед новой попыткой

  try {
    const response = await fetch(apiUrl); // Выполняем HTTP-запрос

    if (!response.ok) { // Проверяем успешность ответа (коды 2xx)
      throw new Error(`Ошибка HTTP: ${response.status} ${response.statusText}`);
    }

    const json = await response.json(); // Парсим JSON из ответа
    apiData.value = json; // Сохраняем данные в реактивную переменную
  } catch (err) {
    error.value = `Не удалось загрузить данные: ${err.message}`; // Обработка ошибок сети или парсинга
    console.error('Ошибка загрузки API:', err);
  } finally {
    loading.value = false; // Завершаем загрузку, независимо от результата
  }
};

// 3. Вызов функции загрузки данных при монтировании компонента
onMounted(() => {
  fetchData();
});


const _piUrl = import.meta.env.VITE_API_URL
const _appName = import.meta.env.VITE_APP_NAME
const _isDebug = import.meta.env.VITE_DEBUG
////////// - TEST END
</script>

<template>
  <div class="greetings">
    <h1 class="green">{{ msg }} - {{ _appName }}</h1>
    <h3>
      You’ve successfully created a project with
      <a href="https://vite.dev/" target="_blank" rel="noopener">Vite</a> +
      <a href="https://vuejs.org/" target="_blank" rel="noopener">Vue 3</a>.
    </h3>
    <h3>
      Work with API:
      <a href="http://api.localhost/docs" target="_blank" rel="noopener">Dev</a> |
      <a href="http://api-qa.[domain].com/docs" target="_blank" rel="noopener">QA</a> |
      <a href="https://api.[domain].com/docs" target="_blank" rel="noopener">Prod</a>
    </h3>
    <h3>
      API version: <b v-if="apiData">{{ apiData.data['version'] }}</b>
    </h3>
    
    <p v-if="loading">Loading data ...</p>
    <p v-if="error">{{ error }}</p>
    
    <div v-if="apiData">
      <pre>{{ JSON.stringify(apiData, null, 2) }}</pre>
    </div>

  </div>
</template>

<style scoped>
h1 {
  font-weight: 500;
  font-size: 2.6rem;
  position: relative;
  top: -10px;
}

h3 {
  font-size: 1.2rem;
}

.greetings h1,
.greetings h3 {
  text-align: center;
}

@media (min-width: 1024px) {
  .greetings h1,
  .greetings h3 {
    text-align: left;
  }
}
</style>
