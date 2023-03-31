int num, i = 0;
    time_t start, current;
    double elapsed_time, max_time = 10.0; // tempo limite em segundos
    
    time(&start); // obtém o tempo inicial
    
    while (1) {
        // obtém o tempo atual e calcula o tempo decorrido
        time(&current);
        elapsed_time = difftime(current, start);
        
        if (elapsed_time >= max_time) { // se o tempo limite foi atingido
            printf("Tempo limite atingido.\n");
            break; // sai do loop
        }
        