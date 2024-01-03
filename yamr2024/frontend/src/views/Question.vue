<template>
    <div class="container mt-3">
        <div v-if="question">
            <h2>{{ question.content }}</h2>
            <p>Posted by: <span class="author-name">{{ question.author }}</span></p>
            <p>{{ question.created_at }}</p>
            <hr>
        </div>
        <div v-else>
            <h2 class="error text-center">404 - Question Not Found</h2>
        </div>

        <div v-if="question">
            <AnswerComponent v-for="answer in answers" :key="answer.uuid" :answer="answer" />
        </div>

        <div class="my-4">
            <p v-show="loadingAnswers">...loading...</p>
            <button v-show="next" @click="getQuestionAnswer" class="btn btn-sm btn-outline-success">
                Load More Answers
            </button>
        </div>
    </div>
</template>

<script>
import { axios } from '@/common/api.service.js'
import AnswerComponent from '@/components/Answer.vue'
export default {
    name: 'QuestionView',
    props: {
        slug: {
            type: String,
            required: true,
        },
    },
    components: {
        AnswerComponent
    },
    data() {
        return {
            question: [],
            answers: [],
            next: null,
            loadingAnswer: false
        }
    },
    methods: {
        setPageTitle(title) {
            document.title = `${title} - YAMR`;
        },
        async getQuestionData() {
            // get the details of a question instance from the REST API and call setPageTitle
            let endpoint = `/api/v1/questions/${this.slug}/`;
            this.loadingAnswer = true;
            try {
                let response = await axios.get(endpoint);
                this.question = response.data;
                this.setPageTitle(this.question.content);
                this.loadingAnswer = false;
                console.log(this.question);
            } catch (error) {
                console.log(error.response);
                const title = error.response.status === 404 ? '404 - Question Not Found' : 'Oops!';
                this.setPageTitle(title);
                // alert(error.response.statusText);
            }
        },
        async getQuestionAnswer() {
            // get a page of answers for a single question from the REST API's paginated 'Questions Endpoint'
            let endpoint = `/api/v1/questions/${this.slug}/answers/`;
            if (this.next) {
                endpoint = this.next;
            }
            this.loadingAnswers = true;
            try {
                let response = await axios.get(endpoint);
                this.answers.push(...response.data.results); // So that we can append the next page to the current page
                this.loadingAnswers = false;
                console.log(this.answers);
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
    created() {
        console.log('QuestionView created... lifecycle hook');
        this.getQuestionData();
        this.getQuestionAnswer();
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