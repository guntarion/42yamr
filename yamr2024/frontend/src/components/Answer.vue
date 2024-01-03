<template>
    <div>
        <p class="text-muted">Author {{ answer.author }} &#8901; {{ answer.created_at }}</p>
        <p style="white-space: pre-wrap;">{{ answer.yamrbody }}</p>
        <hr>

    </div>
</template>

<script>
export default {
    name: "AnswerComponent",
    props: {
        answer: {
            type: Object,
            required: true
        }
    },
}
</script>