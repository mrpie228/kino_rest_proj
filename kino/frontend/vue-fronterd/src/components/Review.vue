<template>
<div>
    <form action="" method="">
        <textarea v-model="text" required></textarea>
        <button type="button" @click="sendReview">Send</button>
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
                movie:this.movie,
                }
                fetch (`http://127.0.0.1:8000/api/v2/review/`,
                    {method:"POST",
                    headers:{
                        'Content-Type':'application/json'
                    },
                    body: JSON.stringify(data)
                    }).then(response=>{console.log(response.json())
                    this.$emit('reLoad')
                    })
            },

        }
    
}
</script>