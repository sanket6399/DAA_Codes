public class WordCount {
	public static void main(String[] args) throws Exception {
		Pipeline pipeline = new MRPipeline(WordCount.class);
		PCollection<String> lines = pipeline.readTextFile(args[0]);
		PCollection<String> words = lines.parallelDo(new DoFn<String, String>() {
			public void process(String line, Emitter<String> emitter) {
				for (String word : line.split("\\s+")) {
					emitter.emit(word);
				}
			}
		}, Writables.strings());
	PTable<String, Long> counts = Aggregate.count(words);
	pipeline.writeTextFile(counts, args[1]);
	pipeline.done();
	}
}