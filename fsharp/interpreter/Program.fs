
type Token(typ, value) =
    member this.Type = typ
    member this.Value = value
    member this.ToString =  sprintf "Type: %s, Value: %O" this.Type this.Type

    
[<EntryPoint>]
let main argv = 
    printfn "%A" argv
    
    let t = Token("INTEGER", 5)
    printf "%O" t
    
    0 // return an integer exit code
