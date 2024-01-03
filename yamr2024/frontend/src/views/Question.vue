<template>
      <div class="container mt-3">
        <div v-if="question">
            <h2>{{ question.content }}</h2>
            <p>Posted by: <span class="author-name">{{ question.author }}</span></p>
            <p>{{  question.created_at }}</p>
        </div>
        <div v-else>
            <h2 class="error text-center">404 - Question Not Found</h2>
      </div>
    </div>
</template>

<script>
import { axios } from '@/common/api.service.js'
export default {
  name: 'QuestionView',
  props: {
    slug: {
      type: String,
      required: true,
    },
  },
    data () {
        return {
        question: null,
        loadingQuestion: false
        }
    },
    methods: {
        setPageTitle (title) {
            document.title = `${title} - YAMR`;
        },
        async getQuestionData () {
            let endpoint = `/api/v1/questions/${this.slug}/`;
            this.loadingQuestion = true;
            try {
                let response = await axios.get(endpoint);
                this.question = response.data;
                this.setPageTitle(this.question.content);
                this.loadingQuestion = false;
                console.log(this.question);
            } catch (error) {
                console.log(error.response);
                const title = error.response.status === 404 ? '404 - Question Not Found' : 'Oops!';
                this.setPageTitle(title);
                // alert(error.response.statusText);
            }
        }
    },
    created () {
        console.log('QuestionView created... lifecycle hook');
        this.getQuestionData();
    }
  
}
</script>

<style>
.author-name {
  font-weight: bold;
  color: #dc3545;
}
.error {
  color: #dc3545;
}

</style>