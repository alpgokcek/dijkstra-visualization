N = [10, 50, 100, 200, 500, 1000];
actual_times = [0.00012, 0.000382, 0.00084, 0.0021, 0.00977, 0.0351];
plot(N, times, 'r', 'linewidth', 2)
xlabel('|V| (# of vertices)'); ylabel('Time (seconds)')