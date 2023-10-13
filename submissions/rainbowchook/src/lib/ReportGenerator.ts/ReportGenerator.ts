import { RowItem } from '../readers/RowItem'
import { Analyser } from '../analysers/Analyser'
import { Reporter } from '../reporters/Reporter'

export class ReportGenerator {
  constructor(public analyser: Analyser<RowItem>, public reporter: Reporter) {}

  buildAndPrintAnalysisReport(tracks: RowItem[]) {
    const analysis = this.analyser.run(tracks)
    this.reporter.print(analysis)
  }
}
