<template>
<div>
    <form action="" method="">
        <textarea v-model="text"></textarea>
        <button>Send</button>
    </form>
   <div class="review" v-for="review in reviews" :key="review.id">
       <div class="one_review">
       <img src="../assets/logo.png" width="50">
       <a>{{review.name}} <a> </a></a>
       <a>{{review.text}}</a>
       <div class="children review" v-for="child in review.children">
           <img src="../assets/logo.png" width="50">
           <a v-if="child.name !=''">{{child.name}}</a>
           <a v-else>Moderator </a>
           <a>{{child.text}} <a> </a></a>
           <a>*that child*</a>
           </div>
       </div>
   </div>
</div>
</template>


<script>
export default {
    name: "Review",
    props:["reviews","movie"],
    data() {
        return {
            name:'',
            email:'',
            text:'',
            parent:null,

        }
    },
    methods: {
        async sendReview(){
            let data= {
                text: this.text,
                parent:this.parent,
                }
            },

        }
    },
}
</script>