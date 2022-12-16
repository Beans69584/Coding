class Countdown {
        static void Main() {
            while (true) {  // Loop forever (or until Ctrl-C) 
                DateTime dateInTheFuture = new DateTime(2022, 12, 25);
                DateTime dateToday = DateTime.Now;
                TimeSpan timeSpan = dateInTheFuture - dateToday;
                Console.Clear();
                Console.WriteLine("Until Christmas 2022:\n" + timeSpan.Days + " days " + timeSpan.Hours + " hours " + timeSpan.Minutes + " minutes " + timeSpan.Seconds + " seconds" );
                System.Threading.Thread.Sleep(1000);
        }
    }
}