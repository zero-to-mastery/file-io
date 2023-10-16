import { RowItem } from '../readers/RowItem'
import { Analyser } from '../analysers/Analyser'
import { Reporter } from '../reporters/Reporter'
import { ConsoleReport } from '../reporters/ConsoleReporter'
import { HTMLReporter } from '../reporters/HTMLReporter'

export class ReportGenerator {
  constructor(public analyser: Analyser<RowItem>, public reporter: Reporter) {}

  static forConsole(analyser: Analyser<RowItem>) {
    return new ReportGenerator(analyser, new ConsoleReport())
  }

  static forHTML(analyser: Analyser<RowItem>) {
    return new ReportGenerator(analyser, new HTMLReporter())
  }

  buildAndPrintAnalysisReport(tracks: RowItem[]) {
    const analysis = this.analyser.run(tracks)
    this.reporter.print(analysis)
  }
}
