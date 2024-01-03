<template>
  <div class="home mt-3">
    <!-- <h1>Homepage</h1> -->
    <!-- <button class="btn btn-primary" @click="getQuestions">Get Questions</button> -->
    <!-- <div v-if="this.questions">
      {{ this.questions }}
    </div> -->
    <div class="container">
      <div v-for="question in questions" :key="question.pk">
          <div class="card shadow p-3 mb-4 bg-body rounded">
            <div class="card-body">
              <p class="card-title">Posted by: <span class="question-author">{{ question.author }}</span></p>
              <router-link :to="{ name: 'question', params: { slug: question.slug } }" class="question-link">
                <h5 class="card-title">{{ question.content }}</h5>
              </router-link>
              <p class="mb-2">Answers: {{ question.yamr_answers_count }}</p>
              <a href="#" class="btn btn-primary">Go somewhere</a>
            </div>
          </div> 
      </div>
       <div class="my-4">
        <p v-show="loadingQuestions">...loading...</p>
        <button
          v-show="next"
          @click="getQuestions"
          class="btn btn-sm btn-outline-success"
        >
          Load More
        </button>
      </div>

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
      questions: [],
      next: null,
      loadingQuestions: false
    }
  },
  methods: {
    async getQuestions () {
      let endpoint = '/api/v1/questions/';
      if (this.next) {
        endpoint = this.next;
      }
      this.loadingQuestions = true;
      try {
        let response = await axios.get(endpoint);
        // console.log(response);
        // this.questions = response.data; // Before adding pagination
        // this.questions = response.data.results; // After adding pagination
        this.questions.push(...response.data.results); // So that we can append the next page to the current page
        this.loadingQuestions = false;
        console.log(this.questions);
        if (response.data.next) {
          this.next = response.data.next;
        } else {
          this.next = null;
        }
      } catch (error) {
        console.log(error.response);
        alert(error.response.statusText);
      }
    }
  },
  created () {
    document.title = 'YAMR';
    console.log('HomeView created... lifecycle hook');
    this.getQuestions();
  }
}
</script>

<style scoped>
.question-author {
  font-weight: bold;
  color: #dc3545;
}

.question-link {
  font-weight: 400;
  color: black;
  text-decoration: none;
}

.question-link:hover {
  color: #343a40;
}
</style>