![Pomodoro Technique](https://blog.trello.com/hs-fs/hubfs/Imported_Blog_Media/pomodoro_feature-640x360.jpg?width=640&name=pomodoro_feature-640x360.jpg "Pomodoro Technique")

# Tecnica Pomodoro

La tecnica pomodoro esta orientada a mejorar la productividad de una forma rapida y efectiva. [Mas info](https://blog.trello.com/es/tecnica-pomodoro)

## Implementacion 

Esta aplicacion de escritorio muestra notificaciones de **W10** al iniciar un evento de la tecnica pomodoro. 
> - Al inciar pomodoro
> - Descanso entre pomodoro
> - Descanso entre set de pomodoros

### Ejemplo
![Pomodoro Example](/assets/img/start.png "Pomodoro Example")


## Configuracion General
``` js
{
    "max_iterations":4 default,
    "study_time":"30m" default,
    "little_break_time": "8m" default,
    "break_time": "20m" default
}
```
- **max_iterations**: Cantidad de pomodoros que conforman un set
- **study_time**: Duracion de un pomodoro
- **little_break_time**: Descanso entre cada pomodoro
- **break_time**: Descanso entre cada set de pomodoros

## Ejecucion
```python 
python StudyTime.py
```
 
