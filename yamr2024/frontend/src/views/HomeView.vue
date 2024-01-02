<template>
  <div class="home">
    <h1>Homepage</h1>
    <button class="btn btn-primary" @click="getQuestions">Get Questions</button>
    <div v-if="this.questions">
      {{ this.questions }}
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import { axios } from '@/common/api.service.js'
export default {
  name: 'HomeView',
  data () {
    return {
      questions: []
    }
  },
  methods: {
    async getQuestions () {
      let endpoint = '/api/v1/questions/';
      try {
        let response = await axios.get(endpoint);
        // console.log(response);
        this.questions = response.data;
        console.log(this.questions);
      } catch (error) {
        console.log(error.response);
        alert(error.response.statusText);
      }
    }
  },
}
</script>
