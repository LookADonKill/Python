murid = [
{
    "nama":'Juan',
    "umur": 16,
    "NIS": 1913764
},
{
    "nama":'Enryl',
    "umur": 17,
    "NIS": 1911892
}
]

for kanisian in murid:
    for key, value in kanisian.items():
        print(f'{key} : {value}')