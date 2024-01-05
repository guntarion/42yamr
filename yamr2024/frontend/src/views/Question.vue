<template>
    <div class="container mt-3">
        <div v-if="question">
            <h2>{{ question.content }}</h2>
            <p>Posted by: <span class="author-name">{{ question.author }}</span></p>
            <p>{{ question.created_at }}</p>

            <QuestionActions v-if="isQuestionAuthor" :slug="question.slug" />

            <div v-if="userHasAnswered">
                <p class="answer-text">You have answered this question</p>
            </div>
            <div v-else-if="showForm">
                <form @submit.prevent="onSubmit">
                    <p>Answer the Question</p>
                    <div class="mb-3">
                        <label for="answer" class="form-label">Answer</label>
                        <textarea v-model="newAnswerBody" class="form-control" placeholder="your answer"
                            rows="3"></textarea>
                    </div>
                    <button type="submit" class="btn btn-primary">Submit</button>
                    <button class="btn btn-danger" @click="showForm = false">Cancel</button>
                </form>
                <p v-if="error" class="error mt-2">{{ error }}</p>
            </div>
            <div v-else>
                <button class="btn btn-success" @click="showForm = true">
                    Answer this question
                </button>
            </div>

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
import QuestionActions from '@/components/QuestionActions.vue'

export default {
    name: 'QuestionView',
    props: {
        slug: {
            type: String,
            required: true,
        },
    },
    components: {
        AnswerComponent,
        QuestionActions
    },
    data() {
        return {
            question: [],
            answers: [],
            next: null,
            loadingAnswer: false,
            userHasAnswered: false,
            showForm: false,
            newAnswerBody: '',
            error: null
        }
    },
    computed: {
        isQuestionAuthor() {
            // return true if the logged in user is also the author of the question instance
            return this.question.author === this.requestUser;
        },
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
        },
        async onSubmit() {
            // Tell the REST API to create a new answer for this question
            // based on the user input, then update some data properties
            if (!this.newAnswerBody) {
                this.error = "You can't send an empty answer!";
                return;
            }
            const endpoint = `/api/v1/questions/${this.slug}/answer/`;
            try {
                const response = await axios.post(endpoint, {
                    yamrbody: this.newAnswerBody,
                });
                this.answers.unshift(response.data);
                // unlike the push method which adds elements to the end of an array, unshift adds elements to the beginning.
                this.newAnswerBody = null;
                this.showForm = false;
                this.userHasAnswered = true;
                if (this.error) {
                    this.error = null;
                }
            } catch (error) {
                console.log(error.response);
                alert(error.response.statusText);
            }
        },
        setRequestUser() {
            // the username has been set to localStorage by the App.vue component
            this.requestUser = window.localStorage.getItem("username");
        },
    },
    created() {
        console.log('QuestionView created... lifecycle hook');
        this.getQuestionData();
        this.getQuestionAnswer();
        this.setRequestUser();
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

.answer-text {
    font-weight: bold;
    color: #17b993;
}
</style>