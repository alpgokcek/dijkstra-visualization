N = [10, 50, 100, 200, 500, 1000];
theoritical_times = [35, 290, 692, 1650, 4725, 11500] .* 0.00001;
actual_times = [0.00012, 0.000382, 0.00084, 0.0021, 0.00977, 0.0351];

figure
plot(N, actual_times, 'r', 'linewidth', 2);
hold on
plot(N, theoritical_times, 'g', 'linewidth', 2);
legend('Observed Time','Theoretical Time');
xlabel('|V| (# of vertices)'); ylabel('Time (seconds)')