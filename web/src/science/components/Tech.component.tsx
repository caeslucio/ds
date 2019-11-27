import m from 'mithril';
import { MithrilTsxComponent as Component } from 'mithril-tsx-component';


class Tech extends Component {
    title: string;
    money: string;
    myClass: string;

    constructor(vnode){
        super();
    }

    toggle(){
        const elements = document.querySelectorAll(".tech-btn") as Array ;
        elements.map(
            element => {
                element.style.animation = "";
            }
        )
    }

    view(vnode){

        const element = document.querySelectorAll(".tech-btn");
        var isDisabled;
        if (vnode.attrs.status === "2"){
            isDisabled = " unTech";
        }else{
            isDisabled = "";
        }

        return <button style={{animation: "textShadow 1.6s infinite"}} onclick={vnode.attrs.changeHandler} class={`nes-btn tech-btn ${vnode.attrs.type} ${isDisabled}`}>
            <div class="TechText"><p class="TechTitle">{vnode.attrs.title}</p>
            <p>R${`${vnode.attrs.money}`}</p></div>
        </button>
    }
}

export default Tech;